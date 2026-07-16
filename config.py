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

# 필수 및 설정 변수 정의
API_ID = int(os.environ.get('API_ID', 0))
API_HASH = os.environ.get('API_HASH', "")
BOT_TOKEN = os.environ.get('BOT_TOKEN', "")
DATABASE_URI = os.environ.get('DATABASE_URI', "")
DATABASE_NAME = os.environ.get('DATABASE_NAME', "BetterAutoFilterBot")

# main.py에서 호출하는 변수들 추가
AUTH_CHANNEL = os.environ.get('AUTH_CHANNEL', None)
AUTH_USERS = [int(x) for x in os.environ.get('AUTH_USERS', "").split()]
CUSTOM_FILE_CAPTION = os.environ.get('CUSTOM_FILE_CAPTION', None)
API_KEY = os.environ.get('API_KEY', None)
AUTH_GROUPS = [int(x) for x in os.environ.get('AUTH_GROUPS', "").split()]
DEV_CHANNEL = os.environ.get('DEV_CHANNEL', "https://t.me/ZauteKm")

print("✅ 환경 변수 로딩 성공.")
