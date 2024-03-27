from contextlib import asynccontextmanager

import motor.motor_asyncio
from beanie import init_beanie
from fastapi import FastAPI
from pydantic_settings import BaseSettings

from src.beaniecocktails.models import Cocktail
from src.beaniecocktails.routers import cocktail_router


class Settings(BaseSettings):
    mongodb_uri: str = "mongodb://localhost:27017/cocktails"


@asynccontextmanager
async def lifespan(app: FastAPI):
    client = motor.motor_asyncio.AsyncIOMotorClient(Settings().mongodb_uri)
    await init_beanie(client.get_default_database(), document_models=[Cocktail])
    app.include_router(cocktail_router, prefix="/v1")
    yield


app = FastAPI(lifespan=lifespan)
