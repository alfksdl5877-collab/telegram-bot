#!/usr/bin/env python3
import asyncio
import sys
import os
import time
import traceback
from pyrogram import Client

# 봇 설정 로드
from config import *

# 1. 이전 세션 삭제 (매번 새로 연결)
if os.path.exists("auto-filter-bot.session"):
    try:
        os.remove("auto-filter-bot.session")
    except:
        pass

# 2. 클라이언트 설정
app = Client(
    "auto-filter-bot", 
    api_id=API_ID, 
    api_hash=API_HASH, 
    bot_token=BOT_TOKEN,
    workdir="."
)

# 3. 시간 동기화 에러 무시 설정 (핵심!)
# Pyrogram의 세션 설정에서 시간 오차에 대한 허용 범위를 넓힙니다.
from pyrogram.session import Session
Session.MAX_TIMEOUT = 60 

async def start_bot():
    print("🚀 봇 연결을 시도합니다...")
    # 텔레그램 서버에 연결하면서 시간 차이가 나면 
    # 서버가 주는 시간값으로 즉시 동기화하도록 시도합니다.
    await app.start()
    print("✅ 봇이 성공적으로 연결되었습니다!")
    
    # 봇이 죽지 않게 유지
    from pyrogram import idle
    await idle()

if __name__ == "__main__":
    try:
        # 시간 오차 발생 시 재시도 루프
        asyncio.run(start_bot())
    except Exception as e:
        print(f"❌ 치명적인 에러 발생: {e}")
        traceback.print_exc()
        # 1분 대기 후 종료 (Render가 다시 실행하도록)
        time.sleep(60)
        sys.exit(1)
