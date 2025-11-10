from . import db
from .base import BaseModel
from sqlalchemy.orm import validates, relationship

class Category(BaseModel):
    """
    Category model representing a game category for crowdfunding projects.
    
    A category can have multiple games and includes information
    about the category's name and description.
    """
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)
    
    # One-to-many relationship: one category has many games
    games = relationship("Game", back_populates="category")
    
    @validates('name')
    def validate_name(self, key: str, name: str) -> str:
        """
        Validate the category name field.
        
        Args:
            key: The name of the field being validated.
            name: The category name to validate.
            
        Returns:
            The validated category name.
        """
        return self.validate_string_length('Category name', name, min_length=2)
        
    @validates('description')
    def validate_description(self, key: str, description: str | None) -> str | None:
        """
        Validate the category description field.
        
        Args:
            key: The name of the field being validated.
            description: The category description to validate.
            
        Returns:
            The validated category description.
        """
        return self.validate_string_length('Description', description, min_length=10, allow_none=True)
    
    def __repr__(self) -> str:
        """
        Return a string representation of the Category instance.
        
        Returns:
            A string showing the category name.
        """
        return f'<Category {self.name}>'
        
    def to_dict(self) -> dict:
        """
        Convert the Category instance to a dictionary for JSON serialization.
        
        Returns:
            A dictionary containing the category data including the count of associated games.
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'game_count': len(self.games) if self.games else 0
        }