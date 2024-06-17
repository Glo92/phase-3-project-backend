from fastapi import FastAPI, Depends
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from models.category import Category
from models.shoes import Shoes
from models.shoe import Shoe
from models.users import User
from validation_model import ShoeModel,UserModel
from db import cursor,conn
from typing import List
import sqlite3

app = FastAPI()
DATABASE_URL = "db.sqlite"

def get_db():
    conn = sqlite3.connect(DATABASE_URL)
    try:
        yield conn
    finally:
        conn.close()


app.add_middleware(CORSMiddleware, allow_origins = ["http://localhost:5173"],allow_credentials = True, allow_methods = ["*"],allow_headers = ["*"],)

@app.get("/shoe", response_model=List[dict])
def get_shoes(db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM shoe")
    rows = cursor.fetchall()

    shoes = []
    for row in rows:
        shoe = {
            "id": row[0],
            "name": row[1],
            "image": row[2],
            "description": row[3],
            "price": row[4],
            "category_id": row[5]
        }
        shoes.append(shoe)

    return shoes



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/category")
def category():
    category = Category.get_all()

    return category


# Post users
@app.post("/users")
def save_user(data:UserModel):
    user = User(data.name, data.phone,data.email,data.password)
    user.save()
    return user.to_dict()

