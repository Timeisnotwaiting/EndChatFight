from mongo import mongo_build

db = mongo_build()

mongodb = db.mongo

async def update(chat_id: int, user_id: int, count: int):
    await mongodb.update_one({"chat_id": chat_id, "user_id": user_id, "count": count}, upsert=True)

async def get_det(chat_id: int, user_id: int):
    stat = mongodb.find_one({"chat_id": chat_id, "user_id": user_id})
    if not stat:
        return 
    return stat["count"]

async def get_stats(chat_id: int):
    stats = mongodb.find_one({"chat_id": chat_id})
    if not stats:
        return
    IDS = []
    COUNTS = []
    async for c in stats:
        IDS.append(c["user_id"])
        COUNTS.append(c["count"])
    return IDS, COUNTS
    
