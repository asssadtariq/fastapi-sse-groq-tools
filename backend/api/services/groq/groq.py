"""This is a service module that interacts with the Groq API."""

import json
from typing import Optional, Union, List

from groq import Groq
from groq.resources.chat.completions import ChatCompletion

from api import settings
from api.services.groq.tools.tools import GroqTools
from api.services.groq.tools.get_weather import get_weather
from api.services.groq.tools.schedule_appointment import schedule_appointment
from api.services.groq.tools.get_dealership_address import get_dealership_address
from api.services.groq.tools.check_appointment_availability import (
    check_appointment_availability,
)


class GroqService:
    def __init__(
        self,
        grq_api_key: str = settings.GROQ_API_KEY,
        grq_model_name: str = settings.GROQ_MODEL_NAME,
    ) -> None:
        self.client = Groq(api_key=grq_api_key)
        self.system_prompt: Optional[str] = (
            "You are an AI assistant, please help me with the following questions:"
        )
        self.model = grq_model_name

    def set_system_prompt(self, str) -> None:
        """This is a setter method for the system prompt."""
        self.system_prompt = str

    def get_llm_message(
        self, user_prompt: Union[List, str], system_prompt: Optional[str] = None
    ) -> List:
        """This method constructs the message object for the LLM API."""

        assert user_prompt, "User prompt cannot be empty"
        assert isinstance(user_prompt, str) or isinstance(user_prompt, list), (
            "User prompt must be a string or a list"
        )
        # user_prompt = user_prompt if isinstance(user_prompt, list) else [user_prompt]
        system_prompt = system_prompt if system_prompt else self.system_prompt

        return [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]

    def call_llm(
        self,
        messages: List,
        model: str,
        tools: Optional[List] = None,
        max_completion_tokens: int = 4096,
        tool_choice: str = "required",
        stream: bool = False,
    ) -> ChatCompletion:
        """This method calls the LLM API with the provided messages."""

        # call the Groq API and get response
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                tools=tools,
                tool_choice=tool_choice,
                stream=stream,
                max_tokens=max_completion_tokens,
            )
        except Exception as e:
            raise Exception(f"Error calling Groq API: {e}")

        # return the response
        return response

    def call_tool(self, query: str, function_name: str) -> str:
        messages = self.get_llm_message(user_prompt=query)

        tools = [
            GroqTools.GET_WEATHER,
            GroqTools.GET_DEALERSHIP_ADDRESS,
            GroqTools.SCHEDULE_APPOINTMENT,
            GroqTools.CHECK_APPOINTMENT_AVAILABILITY,
        ]

        # Make the initial API call to Groq
        response = self.call_llm(model=self.model, messages=messages, tools=tools)

        # Extract the response and any tool call responses
        response_message = response.choices[0].message
        tool_calls = response_message.tool_calls

        if tool_calls:
            # Define the available tools that can be called by the LLM
            available_functions = {
                "get_weather": get_weather,
                "get_dealership_address": get_dealership_address,
                "schedule_appointment": schedule_appointment,
                "check_appointment_availability": check_appointment_availability,
            }
            # Add the LLM's response to the conversation
            messages.append(response_message)

            # Process each tool call
            for tool_call in tool_calls:
                function_name = tool_call.function.name
                function_to_call = available_functions[function_name]
                function_args = json.loads(tool_call.function.arguments)
                # Call the tool and get the response
                try:
                    function_response = function_to_call(**function_args)
                except Exception as e:
                    print(f"Error calling tool: {e}")
                    print(
                        f"Got an error while calling function {function_name} with args {function_args}"
                    )
                    function_response = f"Error calling tool: {e}"

                # convert the response to a string
                function_response = str(function_response)

                # Add the tool response to the conversation
                messages.append(
                    {
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": function_name,
                        "content": function_response,
                    }
                )

        # Make a second API call with the updated conversation
        second_response = self.call_llm(model=self.model, messages=messages)

        return second_response.choices[0].message.content
