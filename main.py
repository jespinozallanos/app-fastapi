from fastapi import FastAPI
import uvicorn 
from models.product import Product
from routers.product import router as product_router

app = FastAPI()


@app.get("/")
def message():
    return "hoola julio mundo k2 tal"


app.include_router(product_router)








