#!/usr/bin/env python3
# Copyright (C) @ZauteKm
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import os

# 환경 변수에서 값 가져오기
API_ID = int(os.environ.get('API_ID', 0))
API_HASH = os.environ.get('API_HASH', "")
BOT_TOKEN = os.environ.get('BOT_TOKEN', "")
DATABASE_URI = os.environ.get('DATABASE_URI', "")
DATABASE_NAME = os.environ.get('DATABASE_NAME', "BetterAutoFilterBot")

# 이번에 에러가 발생한 DB_URL과 SESSION 추가
DB_URL = os.environ.get('DATABASE_URI', DATABASE_URI) # 기존 DATABASE_URI를 사용
SESSION = os.environ.get('SESSION', "AutoFilterBot")

# 이전 단계에서 추가한 설정들
COLLECTION_NAME = os.environ.get('COLLECTION_NAME', "Telegram_files")
USE_CAPTION_FILTER = os.environ.get('USE_CAPTION_FILTER', "False") == "True"

# 기존 변수들
AUTH_USERS = [int(x) for x in os.environ.get('AUTH_USERS', "0").split()]
AUTH_GROUPS = [int(x) for x in os.environ.get('AUTH_GROUPS', "0").split()]
AUTH_CHANNEL = os.environ.get('AUTH_CHANNEL', None)
CUSTOM_FILE_CAPTION = os.environ.get('CUSTOM_FILE_CAPTION', None)
API_KEY = os.environ.get('API_KEY', None)
DEV_CHANNEL = os.environ.get('DEV_CHANNEL', "https://t.me/ZauteKm")

print("✅ 환경 변수 로딩 성공.")
