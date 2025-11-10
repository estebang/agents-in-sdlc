# filepath: server/models/base.py
from . import db

class BaseModel(db.Model):
    """
    Abstract base model class providing common validation methods for all models.
    
    This class serves as a parent for all database models in the application,
    providing shared validation functionality.
    """
    __abstract__ = True
    
    @staticmethod
    def validate_string_length(field_name: str, value: str | None, min_length: int = 2, allow_none: bool = False) -> str | None:
        """
        Validate that a string field meets minimum length requirements.
        
        Args:
            field_name: The name of the field being validated (for error messages).
            value: The string value to validate.
            min_length: Minimum required length for the string (default: 2).
            allow_none: Whether None values are allowed (default: False).
            
        Returns:
            The validated string value, or None if allow_none is True.
            
        Raises:
            ValueError: If value is None when not allowed, not a string, or too short.
        """
        if value is None:
            if allow_none:
                return value
            else:
                raise ValueError(f"{field_name} cannot be empty")
        
        if not isinstance(value, str):
            raise ValueError(f"{field_name} must be a string")
            
        if len(value.strip()) < min_length:
            raise ValueError(f"{field_name} must be at least {min_length} characters")
            
        return value