from datetime import datetime
from pydantic import BaseModel


#  inheritance in python
class User(BaseModel):
    id: int
    name = 'Nabin saud'
    last_logged_in: datetime | None = None
    hobbies: list[str] = []


hobbies = {
    "id": "123",
    "last_logged_in": "2023-08-09 12:12",
    "hobbies": ['coding', 'walking', 'technology']
}

user = User(**hobbies)
print(user.id)
print(user.dict())
print("The json data is", user.json())
