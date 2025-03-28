class GroqTools:
    GET_WEATHER: dict = {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "Name of the city to get the weather for",
                    }
                },
                "required": ["city"],
            },
        },
    }

    GET_DEALERSHIP_ADDRESS: dict = {
        "type": "function",
        "function": {
            "name": "get_dealership_address",
            "description": "Get the address of a dealership",
            "parameters": {
                "type": "object",
                "properties": {
                    "dealership_id": {
                        "type": "string",
                        "description": "ID of the dealership to get the address for",
                    }
                },
                "required": ["dealership_id"],
            },
        },
    }

    SCHEDULE_APPOINTMENT: dict = {
        "type": "function",
        "function": {
            "name": "schedule_appointment",
            "description": "Schedule an appointment at a dealership",
            "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                        "type": "string",
                        "description": "ID of the user to schedule the appointment for",
                    },
                    "dealership_id": {
                        "type": "string",
                        "description": "ID of the dealership to schedule the appointment at",
                    },
                    "date": {
                        "type": "string",
                        "description": "Date of the appointment in YYYY-MM-DD format",
                    },
                    "time": {
                        "type": "string",
                        "description": "Time of the appointment in HH:MM format",
                    },
                    "car_model": {
                        "type": "string",
                        "description": "Model of the car for the appointment",
                    },
                },
                "required": ["user_id", "dealership_id", "date", "time", "car_model"],
            },
        },
    }

    CHECK_APPOINTMENT_AVAILABILITY: dict = {
        "type": "function",
        "function": {
            "name": "check_appointment_availability",
            "description": "Check if an appointment is available at a dealership",
            "parameters": {
                "type": "object",
                "properties": {
                    "dealership_id": {
                        "type": "string",
                        "description": "ID of the dealership to check for availability",
                    },
                    "date": {
                        "type": "string",
                        "description": "Date of the appointment in YYYY-MM-DD format",
                    },
                },
                "required": ["date", "dealership_id"],
            },
        },
    }
