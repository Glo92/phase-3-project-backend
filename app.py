from fastapi import FastAPI
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from models.category import Category
from models.shoes import Shoes
from validation_model import ShoeModel
from db import cursor,conn





app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins = ["*"],allow_credentials = True, allow_methods = ["*"],allow_headers = ["*"],)



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/category")
def category():
    category = Category.get_all()

    return category

@app.get("/shoes", response_model=List[dict])
def get_shoes():
    conn.cursor()
    cursor.execute("SELECT * FROM shoes")
    shoes = cursor.fetchall()
    return [dict(zip([column[0] for column in cursor.description], row)) for row in shoes]


@app.post("/shoes")
def save_shoe(data: ShoeModel):
    shoe = Shoes(**data)
    shoe.save()
    return shoe