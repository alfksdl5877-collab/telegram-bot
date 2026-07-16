import os

# 필수 및 설정 변수
API_ID = int(os.environ.get('API_ID', 0))
API_HASH = os.environ.get('API_HASH', "")
BOT_TOKEN = os.environ.get('BOT_TOKEN', "")
DATABASE_URI = os.environ.get('DATABASE_URI', "")
DATABASE_NAME = os.environ.get('DATABASE_NAME', "BetterAutoFilterBot")

# 그동안 에러로 나왔던 모든 변수들 통합
COLLECTION_NAME = os.environ.get('COLLECTION_NAME', "Telegram_files")
USE_CAPTION_FILTER = os.environ.get('USE_CAPTION_FILTER', "False") == "True"
DB_URL = os.environ.get('DATABASE_URI', DATABASE_URI)
SESSION = os.environ.get('SESSION', "AutoFilterBot")
ADMINS = [int(x) for x in os.environ.get('ADMINS', "0").split()]

# 기존 변수들
AUTH_USERS = [int(x) for x in os.environ.get('AUTH_USERS', "0").split()]
AUTH_GROUPS = [int(x) for x in os.environ.get('AUTH_GROUPS', "0").split()]
AUTH_CHANNEL = os.environ.get('AUTH_CHANNEL', None)
CUSTOM_FILE_CAPTION = os.environ.get('CUSTOM_FILE_CAPTION', None)
API_KEY = os.environ.get('API_KEY', None)
DEV_CHANNEL = os.environ.get('DEV_CHANNEL', "https://t.me/ZauteKm")

print("✅ 모든 환경 변수 로딩 완료. 봇 시작 시도 중...")
