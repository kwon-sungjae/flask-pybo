# flask-pybo
플라스크를 이용해 간단한 게시판을 만들어보았다.   
HTML, css의 기본적인 구조와 웹 프레임워크를 빠르게 공부하는 것을 목적으로 플라스크를 써보았고   
서버와 DB연동 등 서버와 웹 구현에 대한 내용을 공부할 수 있었다.

# 폴더와 파일 설명
기본적인 플라스크 프로젝트 구조이다.   
1. 데이터베이스를 처리하는 models.py 파일
ORM을 지원하는 파잉썬 데이터베이스 도구인 SQLAlchemy를 사용
모델 기반으로 데이터베이스를 처리
프로젝트에는 "모델 클래스들을 정의할 models.py파일이 필요"

2. 서버로 전송된 폼을 처리하는 forms.py 파일
웹 브라우저에서 서버로 전송된 폼을 처리할 때 WTForms라는 라이브러리를 사용
WTForms 역시 모델 기반으로 폼을 처리
따라서 폼 클래스를 정의할 froms.py 파일이 필요

3. 화면을 구성하는 views 디렉터리
views디렉터리에는 hello_pybo같은 함수들로 구성된 뷰 파일들을 저장함
main.views, question.views, answer.views 등의 뷰 파일을 만들 것

4. CSS, 자바스크립트, 이미지 파일을 저장하는 static 디렉터리
말 그대로 .css, .jh, .jph, .png등을 저장

5. HTML 파일을 저장하는 templates 디렉터리
질문 목록, 질문 상세 등의 HTML파일을 저장
question_list.html, question_detail.hhtml과 같은 탬플릿 파일을 만들어 사용

6. 파이보 프로젝트를 설정하는 config.py 파일
프로젝트 환경을 설정한다.
환경변수, 데이터베이스 등의 설정을 이 파일에 저장
