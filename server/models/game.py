from . import db
from .base import BaseModel
from sqlalchemy.orm import validates, relationship

class Game(BaseModel):
    """
    Game model representing a crowdfunding game project.
    
    A game belongs to one category and one publisher, and includes
    details like title, description, and star rating.
    """
    __tablename__ = 'games'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    star_rating = db.Column(db.Float, nullable=True)
    
    # Foreign keys for one-to-many relationships
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publishers.id'), nullable=False)
    
    # One-to-many relationships (many games belong to one category/publisher)
    category = relationship("Category", back_populates="games")
    publisher = relationship("Publisher", back_populates="games")
    
    @validates('title')
    def validate_name(self, key: str, name: str) -> str:
        """
        Validate the game title field.
        
        Args:
            key: The name of the field being validated.
            name: The game title to validate.
            
        Returns:
            The validated game title.
        """
        return self.validate_string_length('Game title', name, min_length=2)
    
    @validates('description')
    def validate_description(self, key: str, description: str | None) -> str | None:
        """
        Validate the game description field.
        
        Args:
            key: The name of the field being validated.
            description: The game description to validate.
            
        Returns:
            The validated game description.
        """
        if description is not None:
            return self.validate_string_length('Description', description, min_length=10, allow_none=True)
        return description
    
    def __repr__(self) -> str:
        """
        Return a string representation of the Game instance.
        
        Returns:
            A string showing the game title and ID.
        """
        return f'<Game {self.title}, ID: {self.id}>'

    def to_dict(self) -> dict:
        """
        Convert the Game instance to a dictionary for JSON serialization.
        
        Returns:
            A dictionary containing the game data with related publisher and category information.
        """
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'publisher': {'id': self.publisher.id, 'name': self.publisher.name} if self.publisher else None,
            'category': {'id': self.category.id, 'name': self.category.name} if self.category else None,
            'starRating': self.star_rating  # Changed from star_rating to starRating
        }