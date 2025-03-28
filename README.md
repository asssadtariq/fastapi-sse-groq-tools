# Backend

This directory contains the FastAPI backend for the SuperCar Virtual Sales Assistant. It provides a Server-Sent Events (SSE) powered `/query` endpoint to process user queries, stream AI-generated responses, and integrate with various external tools.

## Overview

- **Real-Time Streaming:** The `/query` endpoint streams responses to clients using SSE.
- **Tool Integration:** The backend supports dynamic tool calls, including:
  - `get_weather`
  - `get_dealership_address`
  - `check_appointment_availability`
  - `schedule_appointment`
- **Session Management:** Each client conversation is managed using a unique `session_id` for contextual responses.
- **Robust Error Handling:** Returns meaningful error messages for invalid requests or server errors.
- **Configurable Environment:** Uses environment variables for sensitive configurations such as API keys.

## API Documentation

Detailed API documentation is available in [API_DOCUMENTATION.md](docs/API_DOCUMENTATION.md). This document explains:
- How to call the `/query` endpoint.
- Request and response formats.
- SSE event types (`chunk`, `tool_use`, `tool_output`, and `end`).
- Example usage using `curl`.

## Getting Started

### Prerequisites

- Python 3.8+
- `pip` package manager

### Installation

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
