# FastAPI Ollama Integration

This project is a FastAPI-based service for interacting with a fine-tuned Llama 3.2 (8B-Chat) model hosted using Ollama. The application provides endpoints for streaming and non-streaming responses from the model.
This README is generated with an OpenAI model so don't @ me.

## Features

- **Authentication**: API key-based authentication for secured access.
- **Streaming Responses**: Stream model outputs in real time.
- **Non-Streaming Responses**: Fetch complete responses from the model in one go.
- **Configurable**: Easily configurable using environment variables and `.env` files.

## Tech Stack

- **FastAPI**: Web framework for building APIs.
- **Ollama**: Hosting and serving Llama models using `llama.cpp`.
- **Pydantic**: Data validation and settings management.
- **HTTPX**: Asynchronous HTTP client (replaced by `ollama` client in this app).
- **StreamingResponse**: For real-time streaming of model outputs.

## Installation

### Prerequisites

- Python 3.8 or higher
- `pip` (Python package manager)
- GPU with CUDA (for local Ollama server)
- Installed `llama.cpp` if using manually.

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/fastapi-ollama.git
   cd fastapi-ollama
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file**:
   ```bash
   touch .env
   ```

   Add the following configuration to `.env`:

   ```env
   API_KEY=my-secret-api-key
   OLLAMA_HOST=http://localhost:11434
   ```

5. **Run the application**:
   ```bash
   cd app
   uvicorn app.main:app --reload
   ```

## Endpoints

### 1. **GET /**

Test route to verify the API is running and check authentication.

- **Request**:
  ```http
  GET / HTTP/1.1
  X-API-Key: your-api-key
  ```

- **Response**:
  ```json
  {
    "message": "Hello World",
    "is_allowed": true
  }
  ```

### 2. **GET /generate**

Fetch a complete non-streaming response from the model.

- **Request**:
  ```http
  GET /generate?query=Hello HTTP/1.1
  X-API-Key: your-api-key
  ```

- **Response**:
  ```json
  {
    "role": "assistant",
    "content": "Hello! How can I assist you today?"
  }
  ```

### 3. **GET /generate/stream**

Stream responses in real time as the model generates output.

- **Request**:
  ```http
  GET /generate/stream?query=Tell me a story HTTP/1.1
  X-API-Key: your-api-key
  ```

- **Response** (streamed `X-NDJSON`):
  ```
  data: {"role": "assistant", "content": "Once upon a time..."}

  data: {"role": "assistant", "content": "the end."}
  ```

## Deployment

To deploy the application:

1. Ensure the `.env` file is configured properly.
2. Run the app with production settings:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```