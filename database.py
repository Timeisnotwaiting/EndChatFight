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
    for c in stats:
        IDS.append(c["user_id"])
        COUNTS.append(c["count"])
    return IDS, COUNTS
    
async def reset():
    get_all = mongodb.find({"chat_id": {"$lt": 0}, "user_id": {"$gt": 0}})
    chats = []
    users = []
    for i in await get_all.to_list(length=1000000000):
        chats.append(i["chat_id"])
        users.append(i["user_id"])
    for chat in chats:
        for user in users:
            await mongodb.update_one({"chat_id": chat, "user_id": user, "count": 0}, upsert=True)
    
