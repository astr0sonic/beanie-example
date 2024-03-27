import asyncio

import motor.motor_asyncio
from beanie import init_beanie
from pydantic_settings import BaseSettings

from src.beaniecocktails.models import Cocktail


class Settings(BaseSettings):
    mongodb_uri: str = "mongodb://localhost:27017/cocktails"


async def init_db() -> None:
    client = motor.motor_asyncio.AsyncIOMotorClient(Settings().mongodb_uri)
    await init_beanie(client.get_default_database(), document_models=[Cocktail])

    cocktail = await Cocktail.find_one()
    print(cocktail)


asyncio.run(init_db())
