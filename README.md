# 📝 FlaskBoard: 간단한 Q&A 블로그 웹앱

> 📍 **[👉 배포된 웹사이트 보러가기](https://flask-pybo.onrender.com)**

FlaskBoard는 **Flask와 SQLAlchemy를 활용하여 구현한 블로그형 게시판 시스템**입니다.  
질문과 답변 기능 중심의 커뮤니티 형태로, **사용자 인증**, **CRUD 기능**, **템플릿 분리**, **ORM 적용** 등  
웹 개발의 핵심 요소들을 실제로 구현해보며 학습한 프로젝트입니다.

> 본 프로젝트는 예제를 기반으로 기능을 학습하고 스스로 구조화하여 직접 구현하였습니다.

---

## 📌 주요 기능

- 회원가입 / 로그인 / 로그아웃
- 질문 등록, 조회수 증가, 수정, 삭제
- 답변 등록, 수정, 삭제
- 로그인한 사용자만 글 작성 가능
- 게시글 목록 및 상세 페이지
- 사용자 정의 템플릿 필터 (`datetime`)
- SQLAlchemy ORM 및 Flask-Migrate로 DB 관리

---

## 📁 프로젝트 구조

```
ksj/
│  __init__.py          # 앱 팩토리 패턴 적용, ORM 및 블루프린트 설정
│  models.py            # 질문, 답변, 사용자 모델 정의
│  forms.py             # 질문/답변/사용자 관련 폼 정의
│  filter.py            # 사용자 정의 필터 함수 (datetime 포맷)
│
├─static/               # 정적 파일 (CSS, JS)
│
├─templates/            # 템플릿 파일 (Jinja2)
│  ├─question/          # 질문 관련 페이지
│  ├─answer/            # 답변 관련 페이지
│  └─auth/              # 로그인/회원가입 페이지
│
└─views/                # 블루프린트 기반 뷰 함수 분리
   ├─main_views.py
   ├─question_views.py
   ├─answer_views.py
   └─auth_views.py
migrations/ # Flask-Migrate로 생성된 마이그레이션 파일
venv/ # 가상환경
.gitignore
config.py
ksj.db # SQLite 데이터베이스
manage.py # 앱 실행 파일
Procfile # Render 배포 설정 파일
README.md
requirements.txt # 라이브러리 목록
```

---

## ⚙️ 실행 방법

1. 가상환경 생성 및 패키지 설치
```bash
python -m venv venv
source venv/bin/activate  # (윈도우: venv\Scripts\activate)
pip install -r requirementes.txt
```

2. 환경설정 파일 `config.py` 확인

3. 데이터베이스 초기화
```bash
flask db init
flask db migrate
flask db upgrade
```

4. 앱 실행
```bash
set FLASK_APP=ksj:create_app (윈도우)
set FLASK_ENV=development (윈도우)
python manage.py
```

---

## Render를 통한 배포

1. GitHub 저장소 준비
- 패키지 목록 정리
- Render에서 마이그레이션 없이 동작할 수 있도록 SQLite DB(ksj.db)를 commit/Push (선택)

2. Render 서비스 생성
```bash
pip install -r requirements.txt (Build Command)
gunicorn "manage:create_app()" (Start Command)
```

3. 배포 완료 후 URL 확인
- https://flask-pybo.onrender.com (예시)

---

## 🙋🏻‍♂️ 프로젝트 제작자: 권성재

> Flask 기본기부터 ORM, 블루프린트, 사용자 인증, 필터링 등 실무 기반의 구조를 경험하며 웹앱 전체 구조를 직접 구성했습니다.

- 📌 **모든 기능 직접 구현**
- 📚 예제를 학습한 뒤, 구조를 완전히 재작성하며 실무 감각을 익힘
- 🔐 백엔드 인증부터 프론트 템플릿 구성까지 일괄 구현

---

## 🛠 사용 기술

| 범주 | 기술 |
|------|------|
| Language | Python 3.x |
| Web Framework | Flask |
| ORM | SQLAlchemy |
| DB Migration | Flask-Migrate |
| Form Handling | Flask-WTF |
| Frontend | Bootstrap, HTML5, Jinja2 |
| Auth | 사용자 인증 (Flask-Login 또는 커스텀 구현) |

---

## 📫 Contact

- 📫 이메일: [chris123ag@naver.com] 
- 📱  연락처: 010-9491-0965
- 🔗 GitHub: [https://github.com/kwon-sungjae]

> "웹개발의 본질은 구조화와 사용자 경험이다. 이를 배우기 위한 첫걸음이 이 프로젝트였다."
