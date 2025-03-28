# API Documentation: `/query` Endpoint

## Overview

The `/query` endpoint is a core part of the SuperCar Virtual Sales Assistant backend. It processes user queries, streams responses using Server-Sent Events (SSE), and integrates with tools to provide dynamic responses.

---

## Endpoint Details

### URL
```
POST /query
```

### Description
This endpoint processes user queries and streams responses back to the client using Server-Sent Events (SSE). It supports tool calling functionality to handle specific tasks like fetching weather information, checking appointment availability, and scheduling appointments.

---

## Request

### Headers
| Key           | Value                  |
|---------------|------------------------|
| Content-Type  | `application/json`     |
| Accept        | `text/event-stream`    |

### Body
The request body must be a JSON object with the following fields:

| Field       | Type   | Required | Description                              |
|-------------|--------|----------|------------------------------------------|
| `query`     | string | Yes      | The user's query or message.             |
| `session_id`| string | Yes      | A unique identifier for the conversation session. |

#### Example Request Body
```json
{
  "query": "What is the weather in New York?",
  "session_id": "session-id"
}
```

---

## Response

### Format
The response is streamed as Server-Sent Events (SSE). Each event contains a specific type and associated data.

### Event Types
| Event Type       | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| `chunk`          | Text chunks from the AI assistant.                                         |
| `tool_use`       | Indicates when the AI decides to use a tool (e.g., `get_weather`).         |
| `tool_output`    | The result of a tool execution.                                            |
| `end`            | Signals the end of the response stream.                                    |

### Example SSE Stream
```
event: chunk
data: Hello! I received your query: I am processing your query

event: tool_use
data: get_weather

event: tool_output
data: {"name": "get_weather", "output": {"temperature": "75°F", "city": "New York"}}

event: end
data:
```

---

## Tools

The `/query` endpoint integrates with the following tools:

| Tool Name                     | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| `get_weather`                 | Fetches weather information for a specified city.                          |
| `get_dealership_address`      | Retrieves the address of a dealership based on its ID.                     |
| `check_appointment_availability` | Checks available appointment slots for a dealership on a given date.      |
| `schedule_appointment`        | Schedules an appointment for a test drive.                                 |

---

## Error Handling

### Possible Errors
| Status Code | Description                              |
|-------------|------------------------------------------|
| `400`       | Invalid request body or missing fields. |
| `500`       | Internal server error.                  |

### Example Error Response
```json
{
  "detail": "Invalid request body. 'query' field is required."
}
```

---

## Example Usage

### Request
```bash
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -H "Accept: text/event-stream" \
  -d '{"query": "What is the weather in New York?", "session_id": "test-session"}'
```

### Response (SSE Stream)
```
event: chunk
data: Hello! I received your query: I am processing your query

event: tool_use
data: get_weather

event: tool_output
data: {"name": "get_weather", "output": {"temperature": "75°F", "city": "New York"}}

event: end
data:
```

---

## Notes

- Ensure that the `session_id` is unique for each conversation to maintain context.
- The endpoint uses the `sse-starlette` library for SSE implementation.
- Tool outputs are dynamically generated based on the query and tool logic.