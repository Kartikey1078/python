from fastapi import  FastAPI
from src.routes.product_routes import product_routes

app = FastAPI(
    title="Fast api course",
    description="topics of fast api"
)

@app.get("/")
def home():
    return {
        "message":"welcome, hi you are here"
    }

app.include_router(product_routes, prefix="/products")