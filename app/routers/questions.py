from flask import Blueprint, request, jsonify
from pydantic import ValidationError

from app.models import db, Question, Category
from app.schemas.question import QuestionCreate, QuestionResponse

questions_bp = Blueprint('questions', __name__, url_prefix='/questions')


@questions_bp.route('/', methods=['GET'])
def get_questions():
    """Get list all questions with info about category."""
    questions = Question.query.all()
    results = [QuestionResponse.from_orm(q).dict() for q in questions]
    return jsonify(results), 200


@questions_bp.route('/', methods=['POST'])
def create_question():
    """Create new questin with search category option."""
    data = request.get_json()
    try:
        question_data = QuestionCreate(**data)
    except ValidationError as e:
        return jsonify(e.errors()), 400

    # If category, check exist or not
    if question_data.category_id is not None:
        category = Category.query.get(question_data.category_id)
        if category is None:
            return jsonify({'message': 'Категория с таким ID не найдена'}), 404

    question = Question(
        text=question_data.text,
        category_id=question_data.category_id
    )
    db.session.add(question)
    db.session.commit()

    return jsonify(QuestionResponse.from_orm(question).dict()), 201