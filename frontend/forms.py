# frontend/forms.py

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser

User = get_user_model()


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Your Name",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Name',
        })
    )
    email = forms.EmailField(
        label="Your Email",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'you@example.com',
        })
    )
    subject = forms.CharField(
        label="Subject",
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Subject',
        })
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Your message…',
        })
    )


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterForm(UserCreationForm):
    TRAVEL_CHOICES = [('', 'Select a travel style')] + list(CustomUser.TRAVEL_STYLE_CHOICES)

    travel_style = forms.ChoiceField(
        choices=TRAVEL_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-input',
            'id': 'travelStyle',
        })
    )
    # … other fields …

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'travel_style', 'password1', 'password2']
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'phone_number', 'travel_style', 'avatar']
        widgets = {
            'email':         forms.EmailInput(attrs={'class':'form-control'}),
            'phone_number':  forms.TextInput  (attrs={'class':'form-control'}),
            'travel_style':  forms.Select     (attrs={'class':'form-select'}),
        }

    avatar = forms.ImageField(required=False, widget=forms.ClearableFileInput)

    # Define the major travel-style choices here:
    TRAVEL_STYLE_CHOICES = [
        ('adventure', 'Adventure'),
        ('luxury', 'Luxury'),
        ('budget', 'Budget'),
        ('family', 'Family'),
    ]
    travel_style = forms.ChoiceField(
        label="Travel Style",
        choices=TRAVEL_STYLE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-input',
            'id': 'register-travel-style',
        })
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Password',
            'id': 'register-password1',
        })
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Confirm password',
            'id': 'register-password2',
        })
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'phone_number',
            'travel_style',
            'password1',
            'password2',
        ]
