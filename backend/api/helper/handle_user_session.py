from typing import Any, AsyncGenerator, Dict, List


async def streaming_generator(
    response: AsyncGenerator[Dict[str, Any], None], stored_responses: List
):
    """Wraps response generator to store data while streaming."""
    async for event in response:
        stored_responses.append(event.data)  # Store data in memory/session
        yield event  # Continue yielding to client
