from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
import os

URL = os.getenv("MONGO_DB_URL")

def mongo_build():
    mongo = MongoClient(URL)
    return mongo.ECF
