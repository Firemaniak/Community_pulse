from flask import Blueprint, request, jsonify
from pydantic import ValidationError

from app.models import db, Category
from app.schemas.category import CategoryCreate, CategoryUpdate, CategoryResponse

categories_bp = Blueprint('categories', __name__, url_prefix='/categories')


@categories_bp.route('/', methods=['POST'])
def create_category():
    """Creating new category"""
    data = request.get_json()
    try:
        category_data = CategoryCreate(**data)
    except ValidationError as e:
        return jsonify(e.errors()), 400

    category = Category(name=category_data.name)
    db.session.add(category)
    db.session.commit()

    return jsonify(CategoryResponse.from_orm(category).dict()), 201


@categories_bp.route('/', methods=['GET'])
def get_categories():
    """Get list all catigories."""
    categories = Category.query.all()
    results = [CategoryResponse.from_orm(c).dict() for c in categories]
    return jsonify(results), 200


@categories_bp.route('/<int:id>', methods=['PUT'])
def update_category(id):
    """Update category by ID."""
    category = Category.query.get(id)
    if category is None:
        return jsonify({'message': 'Категория с таким ID не найдена'}), 404

    data = request.get_json()
    try:
        category_data = CategoryUpdate(**data)
    except ValidationError as e:
        return jsonify(e.errors()), 400

    if category_data.name is not None:
        category.name = category_data.name
        db.session.commit()

    return jsonify(CategoryResponse.from_orm(category).dict()), 200


@categories_bp.route('/<int:id>', methods=['DELETE'])
def delete_category(id):
    """Delete category by ID."""
    category = Category.query.get(id)
    if category is None:
        return jsonify({'message': 'Категория с таким ID не найдена'}), 404

    db.session.delete(category)
    db.session.commit()
    return jsonify({'message': f'Категория с ID {id} удалена'}), 200