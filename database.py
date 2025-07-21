from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb+srv://dakshchandra2234:<db_password>@cluster0.bhd2pa4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = AsyncIOMotorClient(MONGO_URI)
db = client["ecommerce"]
