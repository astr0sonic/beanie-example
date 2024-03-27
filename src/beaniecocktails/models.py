from beanie import Document
from pydantic import BaseModel


class IngredientQuantity(BaseModel):
    quantity: str | None
    unit: str | None


class Ingredient(BaseModel):
    name: str
    quantity: IngredientQuantity | None


class Cocktail(Document):
    name: str
    ingredients: list[Ingredient]
    instructions: list[str]

    class Settings:
        name = "recipes"
