#!/usr/bin/env python3
#!/usr/bin/env python3
import asyncio
import sys
import re
import random
import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import UserNotParticipant

from config import *
from plugins import get_filter_results, get_file_details, is_subscribed, get_poster, RATING, GENRES, HELP, ABOUT

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# 세션 파일 강제 정리
if os.path.exists("auto-filter-bot.session"):
    try:
        os.remove("auto-filter-bot.session")
    except:
        pass

# 봇 클라이언트 설정 (workdir="." 설정이 세션 관리에 도움을 줍니다)
app = Client(
    "auto-filter-bot", 
    api_id=API_ID, 
    api_hash=API_HASH, 
    bot_token=BOT_TOKEN,
    workdir="."
)

BUTTONS = {}
BOT = {}

def get_size(size):
    units = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units):
        i += 1
        size /= 1024.0
    return "%.2f %s" % (size, units[i])

def split_list(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

@Client.on_message(filters.text & filters.private & filters.incoming & filters.user(AUTH_USERS) if AUTH_USERS else filters.text & filters.private & filters.incoming)
async def filter(client, message):
    if message.text.startswith("/"): return
    if AUTH_CHANNEL:
        invite_link = await client.create_chat_invite_link(int(AUTH_CHANNEL))
        try:
            user = await client.get_chat_member(int(AUTH_CHANNEL), message.from_user.id)
            if user.status == "kicked": return
        except UserNotParticipant:
            await client.send_message(chat_id=message.from_user.id, text="**Please Join My Updates Channel to use this Bot!**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🤖 Join Updates Channel 📢", url=invite_link.invite_link)]]), parse_mode="markdown")
            return
        except Exception:
            return
    if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text): return
    if 2 < len(message.text) < 100:    
        btn = []
        search = message.text
        zaute_km = f"**🗂️ Title:** {search}\n**⭐ Rating:** {random.choice(RATING)}\n**🎭 Genre:** {random.choice(GENRES)}\n**📤 Uploaded by {message.chat.title}**"
        files = await get_filter_results(query=search)
        if files:
            for file in files:
                btn.append([InlineKeyboardButton(text=f"[{get_size(file.file_size)}] {file.file_name}",callback_data=f"zautekm#{file.file_id}")])
        else:
            return
        
        if not btn: return
        if len(btn) > 10: 
            btns = list(split_list(btn, 10)) 
            keyword = f"{message.chat.id}-{message.message_id}"
            BUTTONS[keyword] = {"total" : len(btns), "buttons" : btns}
            buttons = btns[0].copy()
            buttons.append([InlineKeyboardButton(text="NEXT ⏩",callback_data=f"next_0_{keyword}")])
            buttons.append([InlineKeyboardButton(text=f"📃 Pages 1/{len(btns)}",callback_data="pages")])
        else:
            buttons = btn
            buttons.append([InlineKeyboardButton(text="📃 Pages 1/1",callback_data="pages")])
        
        poster = await get_poster(search) if API_KEY else None
        if poster: await message.reply_photo(photo=poster, caption=zaute_km, reply_markup=InlineKeyboardMarkup(buttons))
        else: await message.reply_text(zaute_km, reply_markup=InlineKeyboardMarkup(buttons))

@Client.on_callback_query()
async def cb_handler(client, query):
    if query.data == "pages": await query.answer()
    elif query.data.startswith("zautekm"):
        _, file_id = query.data.split("#")
        await query.answer()
        await client.send_cached_media(chat_id=query.from_user.id, file_id=file_id)

if __name__ == "__main__":
    try:
        print("🚀 봇을 시작합니다 (3초 대기)...")
        time.sleep(3) # 서버 시스템 상태 안정화를 위한 3초 대기
        app.run(main())
    except Exception as e:
        # ... 이하 동일
