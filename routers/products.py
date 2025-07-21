from fastapi import APIRouter
from models import Product
from pymongo import MongoClient
from bson import ObjectId
from fastapi import APIRouter
from models import Product
from pymongo import MongoClient
from bson import ObjectId

# MongoDB connection
client = MongoClient("mongodb+srv://dakshchandra2234:Daksh22@cluster0.bhd2pa4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["your-database"]
collection = db["products"]

router = APIRouter()

@router.post("/products")
def create_product(product: Product):
    product_dict = product.dict()
    result = collection.insert_one(product_dict)
    return {"message": "Product created", "id": str(result.inserted_id)}

@router.get("/products")
def get_products():
    products = list(collection.find())
    for p in products:
        p["_id"] = str(p["_id"])
    return products

@router.get("/products/{product_id}")
def get_product(product_id: str):
    product = collection.find_one({"_id": ObjectId(product_id)})
    if product:
        product["_id"] = str(product["_id"])
        return product
    return {"error": "Not found"}

@router.delete("/products/{product_id}")
def delete_product(product_id: str):
    result = collection.delete_one({"_id": ObjectId(product_id)})
    if result.deleted_count:
        return {"message": "Deleted"}
    return {"error": "Not found"}
