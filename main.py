from pyrogram import Client, filters
from pyrogram.types import Message
import os
import datetime
from database import *

API_ID = os.getenv("API_ID", None)
API_HASH = os.getenv("API_HASH", None)
BOT_TOKEN = os.getenv("BOT_TOKEN", None)

def new_day():
    hr = datetime.datetime.now().hour
    min = datetime.datetime.now().minute
    if str(hr) == "18" and str(min) == "30":
        return True

app = Client(":CLIENT:", API_ID, API_HASH, BOT_TOKEN)

@app.on_message(group=1)
async def cwf(_, m):
    if not m.from_user:
        return
    if m.sender_chat:
        return
    chat_id = m.chat.id
    user_id = m.from_user.id
    count = await get_det(chat_id, user_id)
    count += 1
    await update(chat_id, user_id, count)
    await global_update(chat_id, user_id, count)
    if new_day():
        await reset()

@app.on_message(filters.command("profile", ["/", "!", "?", "."]))
async def profile(_, m):
    if not m.from_user:
        return
    if m.sender_chat:
        return
    chat_id = m.chat.id
    user_id = m.from_user.id
    count = await get_det(chat_id, user_id)
    global_count = await get_global_profile(chat_id, user_id)
    today_rank = await get_rank(chat_id, user_id)
    global_rank = await get_global_rank(chat_id, user_id)
    title = m.chat.title
    return await m.reply(_PROFILE.format(title, count, today_rank, global_count, global_rank))
    
