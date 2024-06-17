from pydantic import BaseModel

class ShoeModel(BaseModel):
    name: str
    image: str
    description: str
    price: float
    category_id: int

class UserModel(BaseModel):
    name: str
    phone: str
    email: str
    password: str