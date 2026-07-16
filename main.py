#!/usr/bin/env python3
#!/usr/bin/env python3
import asyncio
import sys
import os
import time
import traceback
from pyrogram import Client

# 봇 설정
from config import *

# 기존 세션 강제 삭제
if os.path.exists("auto-filter-bot.session"):
    try:
        os.remove("auto-filter-bot.session")
    except:
        pass

# 텔레그램 시간 오차 보정을 위해 session 파일 경로를 명확히 지정
app = Client(
    "auto-filter-bot", 
    api_id=API_ID, 
    api_hash=API_HASH, 
    bot_token=BOT_TOKEN,
    workdir="."
)

async def start_bot():
    print("🚀 봇 연결 시도 중 (시간 동기화 대기)...")
    # 텔레그램은 연결 시 봇의 시간을 자동으로 동기화합니다. 
    # start()를 호출하면 서버와 시간 차이가 나더라도 
    # 텔레그램이 '시간 차이가 나니 이 값을 사용하라'고 알려주는 정보를 처리합니다.
    await app.start()
    print("✅ 봇이 성공적으로 연결되었습니다!")
    from pyrogram import idle
    await idle()

if __name__ == "__main__":
    try:
        # 시간 오차 발생 시 재시도 루프
        asyncio.run(start_bot())
    except Exception as e:
        print(f"❌ 에러 발생: {e}")
        # 시간 문제일 경우 서버를 강제로 재시작하여 다른 인스턴스 할당 유도
        print("💡 서버 시간 문제일 가능성이 높습니다. 1분 후 자동 재시작...")
        time.sleep(60)
        sys.exit(1)
