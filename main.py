#!/usr/bin/env python3
import asyncio
import sys
import os
import time
from pyrogram import Client

# 설정 로드
from config import *

# 세션 삭제
if os.path.exists("auto-filter-bot.session"):
    try: os.remove("auto-filter-bot.session")
    except: pass

# 클라이언트 생성
app = Client("auto-filter-bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def main():
    await app.start()
    print("✅ 봇이 정상적으로 연결되었습니다!")
    await asyncio.Event().wait() # 봇 유지

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"❌ 에러 발생: {e}")
        time.sleep(60)
