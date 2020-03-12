from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from typing import List

from models.location import Location
from db.locations import locations as location_db

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

@router.get(
    "/locations/", 
    response_model=List[Location], 
    tags=["locations"],
    summary="Test summary",
    response_description="Test response description")
async def locations(token: str = Depends(oauth2_scheme)):
    """
    Description from DocString
    """
    return location_db
