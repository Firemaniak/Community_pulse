from flask import Blueprint

questions_bp = Blueprint('questions', __name__, url_prefix='/questions')


@questions_bp.route('/', methods=['GET'])
def get_questions():
    return "Список всех вопросов"


@questions_bp.route('/', methods=['POST'])
def create_question():
    return "Вопрос создан"