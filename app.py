from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.category import Category

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins = ["*"],allow_credentials = True, allow_methods = ["*"],allow_headers = ["*"],)



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/category")
def category():
    category = Category.get_all()

    return category

    