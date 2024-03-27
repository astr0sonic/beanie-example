from beanie import PydanticObjectId
from fastapi import APIRouter, Depends, HTTPException

from src.beaniecocktails.models import Cocktail

cocktail_router = APIRouter()


async def get_cocktail_by_id(id: PydanticObjectId) -> Cocktail:
    cocktail = await Cocktail.get(id)
    if cocktail is None:
        raise HTTPException(status_code=404, detail="Cocktail not found")
    return cocktail


@cocktail_router.get("/cocktails/{cocktail_id}", response_model=Cocktail)
async def get_cocktail(cocktail: Cocktail = Depends(get_cocktail_by_id)):
    return cocktail


@cocktail_router.get("/cocktails", response_model=list[Cocktail])
async def list_cocktails():
    cocktails = await Cocktail.find_all().to_list()
    return cocktails


@cocktail_router.post("/cocktails", response_model=Cocktail)
async def create_cocktail(cocktail: Cocktail):
    return await cocktail.create()
