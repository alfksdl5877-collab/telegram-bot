#!/usr/bin/env python3
import asyncio
import sys
import os
import time
import re
import random
import traceback
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
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

# 봇 클라이언트 설정
app = Client(
    "auto-filter-bot", 
    api_id=API_ID, 
    api_hash=API_HASH, 
    bot_token=BOT_TOKEN,
    workdir="."
)

async def main():
    print("✅ 봇이 시작되었습니다.")
    from pyrogram import idle
    await idle()

if __name__ == "__main__":
    try:
        print("🚀 봇을 시작합니다 (3초 대기)...")
        time.sleep(3)
        app.start()
        app.run(main())
    except Exception as e:
        print(f"❌ 봇 시작 중 치명적인 에러 발생: {e}")
        traceback.print_exc()
        time.sleep(60)
