from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# Existing registration form
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'phone_number', 'travel_style', 'password1', 'password2')

# ---------- ONBOARDING STEP FORMS ----------

class TravelStyleForm(forms.Form):
    """Step 1: Ask the user’s travel style."""
    TRAVEL_CHOICES = [
        ('adventure', 'Adventure'),
        ('relaxation', 'Relaxation'),
        ('culture',    'Culture'),
    ]
    travel_style = forms.ChoiceField(
        choices=TRAVEL_CHOICES,
        widget=forms.RadioSelect,
        label="What’s your travel style?"
    )

class BudgetForm(forms.Form):
    """Step 2: Ask the user’s budget range."""
    BUDGET_CHOICES = [
        ('low',    'Low (< $500)'),
        ('medium', 'Medium ($500–$1,500)'),
        ('high',   'High (> $1,500)'),
    ]
    budget = forms.ChoiceField(
        choices=BUDGET_CHOICES,
        widget=forms.RadioSelect,
        label="What’s your budget range?"
    )

class DurationForm(forms.Form):
    """Step 3: Ask how long their trip will be."""
    DURATION_CHOICES = [
        ('weekend', 'Weekend (1–2 days)'),
        ('week',    'Week (3–7 days)'),
        ('month',   'Month (8+ days)'),
    ]
    duration = forms.ChoiceField(
        choices=DURATION_CHOICES,
        widget=forms.RadioSelect,
        label="How long is your trip?"
    )

class LanguageForm(forms.Form):
    """Step 4: Ask which languages they speak."""
    LANG_CHOICES = [
        ('en', 'English'),
        ('es', 'Spanish'),
        ('fr', 'French'),
        # add more as needed
    ]
    languages = forms.MultipleChoiceField(
        choices=LANG_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label="Which languages do you speak?"
    )

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Your Name')
    email = forms.EmailField(required=True, label='Your Email')
    subject = forms.CharField(max_length=150, required=True, label='Subject')
    message = forms.CharField(widget=forms.Textarea, required=True, label='Message')