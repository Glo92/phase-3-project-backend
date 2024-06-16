from fastapi import FastAPI
from models.category import Category

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/category")
def category():
    category = Category.get_all()

    return category

    