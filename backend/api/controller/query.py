"""
QueryController is responsible for processing user queries and interacting with tools
to provide responses. It uses Server-Sent Events (SSE) to stream responses back to the client.
Methods:
    __init__():
        Initializes the QueryController and its dependencies.
    process_query(query: str) -> AsyncGenerator[Dict[str, Any], None]:
        Processes the given query by selecting an appropriate tool, invoking it, and streaming
        the results back to the client using SSE.
    call_groq_tool(query: str, function_name: str) -> Dict:
        Calls the GroqService tool with the given query and function name, and returns the result.
    handle_tool_use(query: str, tool_selection: Dict[str, str]) -> AsyncGenerator[ServerSentEvent, None]:
        Handles the execution of the selected tool and streams the tool's output as SSE.
    select_tool(query: str) -> Dict:
        Selects the appropriate tool based on the content of the query. Returns the name of the tool
        to be used.
Attributes:
    groq_service (GroqService):
        An instance of GroqService used to interact with external tools.
"""

import json
from typing import Any, AsyncGenerator, Dict

from sse_starlette import ServerSentEvent
from api.services.groq.groq import GroqService


class QueryController:
    def __init__(self) -> None:
        self.groq_service = GroqService()

    async def process_query(self, query: str) -> AsyncGenerator[Dict[str, Any], None]:
        """
        Asynchronously processes a query and yields server-sent events (SSE) at various stages.
        Args:
            query (str): The input query string to be processed.
        Yields:
            AsyncGenerator[Dict[str, Any], None]: A sequence of server-sent events (SSE)
            represented as dictionaries. The events include:
                - An initial "chunk" event indicating the query has been received.
                - A "tool_use" event with the selected tool for processing the query.
                - Events yielded during the tool usage process.
                - A final "end" event indicating the completion of the query processing.
        Notes:
            This method uses an asynchronous generator to yield events in real-time,
            making it suitable for streaming responses to clients.
        """

        yield ServerSentEvent(
            event="chunk",
            data="Hello! I received your query: I am processing your query",
        )

        tool_selection = self.select_tool(query=query)

        yield ServerSentEvent(event="tool_use", data=tool_selection)

        async for event in self.handle_tool_use(
            query=query, tool_selection=tool_selection
        ):
            yield event

        yield ServerSentEvent(event="end", data="")

    def select_tool(self, query: str) -> Dict:
        """This function selects the appropriate tool based on the content of the query."""

        if "weather" in query.lower():
            return "get_weather"

        elif "appointment" in query.lower() and "availability" in query.lower():
            return "check_appointment_availability"

        elif "appointment" in query.lower() and "schedule" in query.lower():
            return "schedule_appointment"

        elif "dealership" in query.lower():
            return "get_dealership_address"

    async def handle_tool_use(
        self, query: str, tool_selection: Dict[str, str]
    ) -> AsyncGenerator[ServerSentEvent, None]:
        """This function handles the execution of the selected tool and streams the tool's output."""

        output = await self.call_groq_tool(query, tool_selection)

        yield ServerSentEvent(
            event="tool_output",
            data=json.dumps({"name": tool_selection, "output": output}),
        )

    async def call_groq_tool(self, query, function_name) -> Dict:
        """This function calls the GroqService tool with the given query and function name."""
        return self.groq_service.call_tool(query=query, function_name=function_name)
