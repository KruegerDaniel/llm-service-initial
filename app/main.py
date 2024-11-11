from fastapi import FastAPI
from fastapi.params import Depends

from app.auth import get_allowed
from app.routers import public, secure

app = FastAPI()

app.include_router(
    public.router,
    prefix="/api/v1/public"
)

app.include_router(
    secure.router,
    prefix="/api/v1/secure",
    dependencies=[Depends(get_allowed)]
)
