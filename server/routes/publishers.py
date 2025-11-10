"""
Publishers API routes module.
Provides endpoints for managing and retrieving publisher information.
"""

from flask import jsonify, Response, Blueprint
from models import db, Publisher
from sqlalchemy.orm import Query
from typing import List, Dict, Any

# Create a Blueprint for publishers routes
publishers_bp = Blueprint('publishers', __name__)

def get_publishers_base_query() -> Query:
    """
    Get the base query for publishers.
    
    Returns:
        Query: SQLAlchemy query object for publishers
    """
    return db.session.query(Publisher)

@publishers_bp.route('/api/publishers', methods=['GET'])
def get_publishers() -> Response:
    """
    Get all publishers with their ID and name.
    
    Returns:
        Response: JSON response containing list of publishers
    """
    # Use the base query for all publishers
    publishers_query = get_publishers_base_query().all()
    
    # Convert the results to dictionary format
    publishers_list: List[Dict[str, Any]] = [
        {"id": publisher.id, "name": publisher.name} 
        for publisher in publishers_query
    ]
    
    return jsonify(publishers_list)
