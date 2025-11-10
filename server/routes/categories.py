"""
Categories API routes module.
Provides endpoints for managing and retrieving category information.
"""

from flask import jsonify, Response, Blueprint
from models import db, Category
from sqlalchemy.orm import Query
from typing import List, Dict, Any

# Create a Blueprint for categories routes
categories_bp = Blueprint('categories', __name__)

def get_categories_base_query() -> Query:
    """
    Get the base query for categories.
    
    Returns:
        Query: SQLAlchemy query object for categories
    """
    return db.session.query(Category)

@categories_bp.route('/api/categories', methods=['GET'])
def get_categories() -> Response:
    """
    Get all categories with their ID and name.
    
    Returns:
        Response: JSON response containing list of categories
    """
    # Use the base query for all categories
    categories_query = get_categories_base_query().all()
    
    # Convert the results to dictionary format
    categories_list: List[Dict[str, Any]] = [
        {"id": category.id, "name": category.name} 
        for category in categories_query
    ]
    
    return jsonify(categories_list)