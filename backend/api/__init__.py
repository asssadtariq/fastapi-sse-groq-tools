"""
This module initializes the API package by importing and configuring the
project settings.
Classes:
    ProjectSettings: A class that manages the configuration settings
    for the project.
Objects:
    settings: An instance of ProjectSettings used to access the
    project's configuration.
"""

from typing import Dict, List
from api.core.project_settings import ProjectSettings

settings = ProjectSettings()

# to store session data
SESSION_DATA: Dict[str, List] = {}
