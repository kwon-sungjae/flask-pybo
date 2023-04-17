import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'ksj.db')) # SQLite는 주로 소규모 프로젝트에서 사용하는 데이터베이스
SQLALCHEMY_TRACK_MODIFICATIONS = False # 이벤트를 처리하는 옵션
SECRET_KEY = "dev" # CSRF라는 웹 사이트 취약점 공격을 방지하는데 사용됨