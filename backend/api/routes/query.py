"""
This module initializes the FastAPI router for the query endpoint.
The query endpoint is responsible for streaming the response to the user query.
"""

from fastapi import APIRouter
from sse_starlette import EventSourceResponse

from api import SESSION_DATA
from api.schemas.query import QueryRequest
from api.controller.query import QueryController
from api.helper.get_uuid import get_uuid
from api.helper.handle_user_session import streaming_generator

# init FastAPI router
router = APIRouter(prefix="", tags=["Query"])


@router.post(
    "/query", summary="This endpoint is responsible for processing user queries."
)
async def process_query(payload: QueryRequest) -> EventSourceResponse:
    """Route to process user queries."""

    # get uuid
    session_id = str(get_uuid())

    # init new session in SESSION DATA
    SESSION_DATA[session_id] = []

    response = QueryController().process_query(payload.query)

    return EventSourceResponse(
        streaming_generator(
            response=response, stored_responses=SESSION_DATA[session_id]
        )
    )
