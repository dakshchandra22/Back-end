from fastapi import APIRouter
from models import Order
from database import db
from bson import ObjectId

router = APIRouter()

@router.post("/orders")
async def create_order(order: Order):
    result = await db.orders.insert_one(order.dict())
    return {"id": str(result.inserted_id)}

@router.get("/orders/{user_id}")
async def list_orders(user_id: str, limit: int = 10, offset: int = 0):
    query = {"userId": user_id}
    cursor = db.orders.find(query).skip(offset).limit(limit)
    orders = []
    async for order in cursor:
        order_id = order["_id"]
        items = []
        for item in order["items"]:
            product = await db.products.find_one({"_id": ObjectId(item["productId"])})
            product_details = {
                "name": product["name"],
                "id": str(product["_id"])
            } if product else {}
            items.append({"productDetails": product_details, "qty": item["qty"]})
        orders.append({
            "id": str(order_id),
            "items": items
        })

    return {"data": orders, "page": {"next": str(offset + limit), "limit": limit, "previous": offset - limit}}
