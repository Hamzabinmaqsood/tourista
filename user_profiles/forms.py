# user_profiles/forms.py

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()  # This points to your CustomUser model
        fields = ('username', 'email', 'phone_number', 'travel_style', 'password1', 'password2')
