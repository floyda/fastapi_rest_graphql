from typing import List
from pydantic import BaseModel

class Profile(BaseModel):
    ame: str
    profileType: str
    # parameters: List[Parameter]
    # timespans: List[Timespans]

class Location(BaseModel):
    name: str
    siteCode: str
    siteName: str
    siteDescription: str
    siteClient: str
    profiles: List[Profile]

class Locations(BaseModel):
    locations: List[Location]
    
