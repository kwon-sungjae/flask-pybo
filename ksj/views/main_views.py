from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

from ..models import Question

# 블루프린트 : 플라스크에서는 URL과 함수의 매핑을 관리하기 위해 사용하는 도구
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello') # URL매핑을 /hello로 변경
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))
# redirect(URL) - URL로 페이지를 이동
# url_for(라우팅 함수명) - 라우팅 함수에 매핑되어 있는 URL을 리턴

# 질문 상세 페이지
@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get(question_id)
    return render_template('question/question_detail.html', question=question)

