from pydantic import BaseModel

class ShoeModel(BaseModel):
    name: str
    image: str
    description: str
    price: float
    category_id: int
