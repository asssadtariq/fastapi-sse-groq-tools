"""
This module is used to generate a unique identifier (UUID) for various purposes.
"""

import uuid


def get_uuid() -> uuid.UUID:
    return uuid.uuid4()
