from . import db
from .base import BaseModel
from sqlalchemy.orm import validates, relationship

class Publisher(BaseModel):
    """
    Publisher model representing a game publisher seeking crowdfunding.
    
    A publisher can have multiple games and includes information
    about the publisher's name and description.
    """
    __tablename__ = 'publishers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)
    
    # One-to-many relationship: one publisher has many games
    games = relationship("Game", back_populates="publisher")

    @validates('name')
    def validate_name(self, key: str, name: str) -> str:
        """
        Validate the publisher name field.
        
        Args:
            key: The name of the field being validated.
            name: The publisher name to validate.
            
        Returns:
            The validated publisher name.
        """
        return self.validate_string_length('Publisher name', name, min_length=2)

    @validates('description')
    def validate_description(self, key: str, description: str | None) -> str | None:
        """
        Validate the publisher description field.
        
        Args:
            key: The name of the field being validated.
            description: The publisher description to validate.
            
        Returns:
            The validated publisher description.
        """
        return self.validate_string_length('Description', description, min_length=10, allow_none=True)

    def __repr__(self) -> str:
        """
        Return a string representation of the Publisher instance.
        
        Returns:
            A string showing the publisher name.
        """
        return f'<Publisher {self.name}>'

    def to_dict(self) -> dict:
        """
        Convert the Publisher instance to a dictionary for JSON serialization.
        
        Returns:
            A dictionary containing the publisher data including the count of associated games.
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'game_count': len(self.games) if self.games else 0
        }