#!/usr/bin/env python3
import asyncio
import sys
import re
import random
import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import UserNotParticipant

# 모듈 불러오기
from config import *
from plugins import get_filter_results, get_file_details, is_subscribed, get_poster, RATING, GENRES, HELP, ABOUT

# 이벤트 루프 및 세션 초기화
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

if os.path.exists("auto-filter-bot.session"):
    os.remove("auto-filter-bot.session")
    print("🧹 기존 세션 파일을 삭제했습니다. 새로 연결을 시도합니다.")

app = Client("auto-filter-bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
BUTTONS = {}
BOT = {}

# --- 로직 함수들 (split_list, get_size 등) ---
def get_size(size):
    units = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units):
        i += 1
        size /= 1024.0
    return "%.2f %s" % (size, units[i])

def split_list(l, n):
    for i in range(0, len(l), n): yield l[i:i + n]

# --- 이벤트 핸들러들 (@Client.on_message 등) ---
# [여기에 기존에 사용하시던 @Client.on_message 함수들과 @Client.on_callback_query 함수들을 그대로 두시면 됩니다]
# 현재 코드 흐름상 이 위치에 함수들을 배치하세요.

if __name__ == "__main__":
    print("🚀 봇을 시작합니다...")
    app.run()
