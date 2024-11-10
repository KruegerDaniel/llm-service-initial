import logging

import httpx
from fastapi import APIRouter
from fastapi.params import Depends, Query
from starlette.responses import StreamingResponse

from app.auth import get_allowed
from app.config import settings

router = APIRouter()

logger = logging.getLogger("uvicorn")


@router.get("/")
async def get_testroute(is_allowed: bool = Depends(get_allowed)):
    return {"message": "Hello World", "is_allowed": is_allowed}


@router.get("/generate/stream")
async def get_llama_stream(query: str):
    async def event_stream():
        async with httpx.AsyncClient() as client:
            logger.info(f"Sending request with query: {query}")
            response = await client.post(
                settings.external_api_url,
                json={"model": "llama3.2", "prompt": query, "stream": True},
                headers={"Accept": "text/event-stream"},
            )
            async for line in response.aiter_lines():
                if line.strip():  # Skip empty lines
                    logger.info(f"Received: {line}")
                    yield f"data: {line}\n"

    return StreamingResponse(event_stream(), media_type="application/x-ndjson")


@router.get("/generate")
async def get_llama(query: str):
    async with httpx.AsyncClient() as client:
        logger.info(f"Sending request with query: {query}")
        response = await client.post(
            settings.external_api_url,
            json={"model": "llama3.2", "prompt": query, "stream": False},
            headers={"Accept": "application/json"},
        )
        logger.info(f"Received response: {response.json()}")
        return response.json()
