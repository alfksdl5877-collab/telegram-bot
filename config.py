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

# 필수 환경 변수만 안전하게 불러오기
API_ID = int(os.environ.get('API_ID', 0))
API_HASH = os.environ.get('API_HASH', "")
BOT_TOKEN = os.environ.get('BOT_TOKEN', "")
DATABASE_URI = os.environ.get('DATABASE_URI', "")
DATABASE_NAME = os.environ.get('DATABASE_NAME', "Cluster0")
ADMINS = [int(x) for x in os.environ.get('ADMINS', "0").split()]

# 봇 연결 확인용 로그
if API_ID != 0 and API_HASH and BOT_TOKEN:
    print("✅ 필수 환경 변수 로딩 성공: 봇을 시작합니다.")
else:
    print("❌ 환경 변수 오류: API_ID, API_HASH, BOT_TOKEN 중 하나가 비어있습니다.")
