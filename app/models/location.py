from typing import List
from pydantic import BaseModel

class Location(BaseModel):
    siteid: str
    description: str
    client: str

class Locations(BaseModel):
    locations: List[Location]
    
