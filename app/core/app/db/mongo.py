from pymongo import MongoClient
from app.core.config import MONGO_URL, DATABASE_NAME

client = MongoClient(MONGO_URL)
db = client[DATABASE_NAME]

products_collection = db["products"]
orders_collection = db["orders"]
