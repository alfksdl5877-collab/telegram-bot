#!/usr/bin/env python3
import asyncio
import sys
import re
import random
import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import UserNotParticipant

# 설정 및 플러그인 로드
from config import *
from plugins import get_filter_results, get_file_details, is_subscribed, get_poster, RATING, GENRES, HELP, ABOUT

# 이벤트 루프 설정
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# 세션 초기화 (시간 동기화 문제 해결)
if os.path.exists("auto-filter-bot.session"):
    os.remove("auto-filter-bot.session")
    print("🧹 기존 세션 파일을 삭제했습니다. 새로 연결을 시도합니다.")

app = Client("auto-filter-bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
BUTTONS = {}
BOT = {}

# --- 로직 함수들 ---
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

# --- 기존 핵심 로직 (선생님 코드 전체) ---
@Client.on_message(filters.text & filters.private & filters.incoming & filters.user(AUTH_USERS) if AUTH_USERS else filters.text & filters.private & filters.incoming)
async def filter(client, message):
    if message.text.startswith("/"): return
    if AUTH_CHANNEL:
        invite_link = await client.create_chat_invite_link(int(AUTH_CHANNEL))
        try:
            user = await client.get_chat_member(int(AUTH_CHANNEL), message.from_user.id)
            if user.status == "kicked":
                await client.send_message(chat_id=message.from_user.id, text="Sorry Sir, You are Banned to use me.", parse_mode="markdown", disable_web_page_preview=True)
                return
        except UserNotParticipant:
            await client.send_message(chat_id=message.from_user.id, text="**Please Join My Updates Channel to use this Bot!**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🤖 Join Updates Channel 📢", url=invite_link.invite_link)]]), parse_mode="markdown")
            return
        except Exception:
            await client.send_message(chat_id=message.from_user.id, text="Something went Wrong.", parse_mode="markdown", disable_web_page_preview=True)
            return
    if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text): return
    if 2 < len(message.text) < 100:    
        btn = []
        search = message.text
        zaute_km = f"**🗂️ Title:** {search}\n**⭐ Rating:** {random.choice(RATING)}\n**🎭 Genre:** {random.choice(GENRES)}\n**📤 Uploaded by {message.chat.title}**"
        files = await get_filter_results(query=search)
        if files:
            for file in files:
                file_id = file.file_id
                filename = f"[{get_size(file.file_size)}] {file.file_name}"
                btn.append([InlineKeyboardButton(text=f"{filename}",callback_data=f"zautekm#{file_id}")])
        else:
            await client.send_sticker(chat_id=message.from_user.id, sticker='CAADBQADcAIAAgNqQVet7IusN5nq9hYE')
            return
        if not btn: return
        if len(btn) > 10: 
            btns = list(split_list(btn, 10)) 
            keyword = f"{message.chat.id}-{message.message_id}"
            BUTTONS[keyword] = {"total" : len(btns), "buttons" : btns}
        else:
            buttons = btn
            buttons.append([InlineKeyboardButton(text="📃 Pages 1/1",callback_data="pages")])
            poster=None
            if API_KEY: poster=await get_poster(search)
            if poster: await message.reply_photo(photo=poster, caption=zaute_km, reply_markup=InlineKeyboardMarkup(buttons))
            else: await message.reply_text(zaute_km, reply_markup=InlineKeyboardMarkup(buttons))
            return
        data = BUTTONS[keyword]
        buttons = data['buttons'][0].copy()
        buttons.append([InlineKeyboardButton(text="NEXT ⏩",callback_data=f"next_0_{keyword}")])
        buttons.append([InlineKeyboardButton(text=f"📃 Pages 1/{data['total']}",callback_data="pages")])
        poster=None
        if API_KEY: poster=await get_poster(search)
        if poster: await message.reply_photo(photo=poster, caption=zaute_km, reply_markup=InlineKeyboardMarkup(buttons))
        else: await message.reply_text(zaute_km, reply_markup=InlineKeyboardMarkup(buttons))

@Client.on_message(filters.text & filters.group & filters.incoming & filters.chat(AUTH_GROUPS) if AUTH_GROUPS else filters.text & filters.group & filters.incoming)
async def group(client, message):
    if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text): return
    if 2 < len(message.text) < 50:    
        btn = []
        search = message.text
        zaute_km = f"**🗂️ Title:** {search}\n**⭐ Rating:** {random.choice(RATING)}\n**🎭 Genre:** {random.choice(GENRES)}\n**📤 Uploaded by {message.chat.title}**"
        nyva=BOT.get("username")
        if not nyva:
            botusername=await client.get_me()
            nyva=botusername.username
            BOT["username"]=nyva
        files = await get_filter_results(query=search)
        if files:
            for file in files:
                btn.append([InlineKeyboardButton(text=f"[{get_size(file.file_size)}] {file.file_name}", url=f"https://telegram.dog/{nyva}?start=zautekm_-_-_-_{file.file_id}")])
        else: return
        if not btn: return
        if len(btn) > 10: 
            btns = list(split_list(btn, 10)) 
            keyword = f"{message.chat.id}-{message.message_id}"
            BUTTONS[keyword] = {"total" : len(btns), "buttons" : btns}
        else:
            buttons = btn
            buttons.append([InlineKeyboardButton(text="📃 Pages 1/1",callback_data="pages")])
            poster=None
            if API_KEY: poster=await get_poster(search)
            if poster: await message.reply_photo(photo=poster, caption=zaute_km, reply_markup=InlineKeyboardMarkup(buttons))
            else: await message.reply_text(zaute_km, reply_markup=InlineKeyboardMarkup(buttons))
            return
        data = BUTTONS[keyword]
        buttons = data['buttons'][0].copy()
        buttons.append([InlineKeyboardButton(text="NEXT ⏩",callback_data=f"next_0_{keyword}")])
        buttons.append([InlineKeyboardButton(text=f"📃 Pages 1/{data['total']}",callback_data="pages")])
        poster=None
        if API_KEY: poster=await get_poster(search)
        if poster: await message.reply_photo(photo=poster, caption=zaute_km, reply_markup=InlineKeyboardMarkup(buttons))
        else: await message.reply_text(zaute_km, reply_markup=InlineKeyboardMarkup(buttons))

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    # (선생님 코드의 콜백 처리 부분 그대로 유지)
    clicked = query.from_user.id
    try: typed = query.message.reply_to_message.from_user.id
    except: typed = query.from_user.id
    if (clicked == typed):
        if query.data.startswith("next"):
            ident, index, keyword = query.data.split("_")
            try: data = BUTTONS[keyword]
            except KeyError:
                await query.answer("You are using this for one of my old message, please send the request again.",show_alert=True)
                return
            if int(index) == int(data["total"]) - 2:
                buttons = data['buttons'][int(index)+1].copy()
                buttons.append([InlineKeyboardButton("⏪ BACK", callback_data=f"back_{int(index)+1}_{keyword}")])
                buttons.append([InlineKeyboardButton(f"📃 Pages {int(index)+2}/{data['total']}", callback_data="pages")])
                await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
                return
            else:
                buttons = data['buttons'][int(index)+1].copy()
                buttons.append([InlineKeyboardButton("⏪ BACK", callback_data=f"back_{int(index)+1}_{keyword}"),InlineKeyboardButton("NEXT ⏩", callback_data=f"next_{int(index)+1}_{keyword}")])
                buttons.append([InlineKeyboardButton(f"📃 Pages {int(index)+2}/{data['total']}", callback_data="pages")])
                await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
                return
        elif query.data.startswith("back"):
            ident
