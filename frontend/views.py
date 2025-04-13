from django.shortcuts import render, redirect
from django.contrib.auth import login
from user_profiles.forms import CustomUserCreationForm  # import your custom form
from django.contrib.auth.decorators import login_required
from local_businesses.models import LocalBusiness
from django.contrib.auth.forms import AuthenticationForm

def landing(request):
    return render(request, 'landing.html')

def onboarding(request):
    # A dummy onboarding view to be enhanced later.
    return render(request, 'onboarding.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Log in the user and redirect to dashboard
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard(request):
    businesses = LocalBusiness.objects.all()[:5]
    return render(request, 'dashboard.html', {
        'featured_businesses': businesses
    })

@login_required
def profile(request):
    return render(request, 'profile.html')


def auth_view(request):
    # We just render the combined template. The actual login/register logic
    # is handled by the 'login' and 'register' views in your urls.py.
    login_form = AuthenticationForm(request, data=request.POST or None)
    register_form = CustomUserCreationForm(request.POST or None)

    return render(request, 'auth.html', {
        'login_form': login_form,
        'register_form': register_form
    })