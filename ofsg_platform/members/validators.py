import re
from django.core.exceptions import ValidationError

class ComplexityValidator:
    """Ensure password has upper, lower, digit, and symbol characters."""

    def __init__(self, min_length=10):
        self.min_length = int(min_length)

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(f'Password must be at least {self.min_length} characters long.')
        if not re.search(r'[A-Z]', password):
            raise ValidationError('Password must contain at least one uppercase letter.')
        if not re.search(r'[a-z]', password):
            raise ValidationError('Password must contain at least one lowercase letter.')
        if not re.search(r'\d', password):
            raise ValidationError('Password must contain at least one digit.')
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError('Password must contain at least one symbol (e.g. !@#$%).')

    def get_help_text(self):
        return (
            f"Your password must be at least {self.min_length} characters long and contain "
            "an uppercase letter, a lowercase letter, a digit, and a symbol."
        )
