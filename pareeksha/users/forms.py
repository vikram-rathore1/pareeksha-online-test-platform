from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

# Forms for admin panel
class CustomUserCreationForm(UserCreationForm):
    """Form to create new user"""

    class Meta:
        model = User
        fields = (
            'email',
        )


class CustomUserChangeForm(UserChangeForm):
    """Form to edit a user from admin"""

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'role'
        )
