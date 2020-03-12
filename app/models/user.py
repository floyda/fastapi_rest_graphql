from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    username: str
    operator_id: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str
