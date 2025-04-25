# backend/app/api/__init__.py

from fastapi import APIRouter

api_router = APIRouter()

from .v1 import api as v1_api

api_router.include_router(v1_api.router, prefix="/v1", tags=["v1"])