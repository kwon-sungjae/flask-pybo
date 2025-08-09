# flask-pybo-master/manage.py
from ksj import create_app  # ksj/__init__.py 내 create_app 함수 임포트

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)