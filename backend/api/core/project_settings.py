"""
This file contains the project settings.
it loads the environment variables from the .env file and defines the project settings.
defines the ProjectSettings class that inherits from BaseSettings from pydantic_settings.
"""

import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class ProjectSettings(BaseSettings):
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY")
    GROQ_MODEL_NAME: str = os.getenv("MODEL_NAME")
