import logging

from fastapi import APIRouter
from fastapi.params import Depends
from ollama import AsyncClient
from starlette.responses import StreamingResponse

from app.auth import get_allowed
from app.config import settings

router = APIRouter()

logger = logging.getLogger("uvicorn")
ollama_client = AsyncClient(host=settings.ollama_host)
model = "llama3.2"


@router.get("/")
async def get_testroute(is_allowed: bool = Depends(get_allowed)):
    return {"message": "Hello World", "is_allowed": is_allowed}


@router.get("/generate/stream")
async def get_llama_stream(query: str):
    async def event_stream():
        async for part in await ollama_client.chat(model=model, messages=[
            {"role": "user", "content": query},
        ], stream=True):
            content = part.get("message", {}).get("content", '')
            if content.strip():
                logger.info(f"Received stream part: {content}")
                yield f"data: {content}\n"

    return StreamingResponse(event_stream(), media_type="application/x-ndjson")


@router.get("/generate")
async def get_llama(query: str):
    logger.info(f"Sending request with query: {query}")
    response = await ollama_client.chat(model=model, messages=[
        {"role": "user", "content": query},
    ])
    logger.info(f"Received response: {response}")
    return response
