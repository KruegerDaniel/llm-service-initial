from http.client import HTTPException

from fastapi import status
from fastapi.params import Security
from fastapi.security import APIKeyHeader

from app.config import settings

api_key_header = APIKeyHeader(name="X-API-Key")

def check_api_key(api_key: str) -> bool:
    return api_key == settings.api_key

def get_allowed(api_key_header: str = Security(api_key_header)):
    if check_api_key(api_key_header):
        return True
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Missing or invalid API key",
    )
