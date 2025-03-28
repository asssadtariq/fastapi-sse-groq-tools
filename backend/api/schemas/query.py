"""This file has pydantic model for validating the query API request/response."""

from typing import Optional
from pydantic import BaseModel


class QueryRequest(BaseModel):
    """This is a Pydantic model for the query request."""

    query: str
    session_id: Optional[str] = None
