from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm
from django.shortcuts import render, redirect
from django.templatetags.static import static
from .models import TripPackage, Trip
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib import messages 
from .forms import LoginForm, RegisterForm
from user_profiles.forms import CustomUserCreationForm  
from django.contrib.auth.decorators import login_required
from local_businesses.models import LocalBusiness
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import AuthenticationForm
from formtools.wizard.views import SessionWizardView
from .models import Trip, Itinerary
from django.utils import timezone

from user_profiles.forms import (
    TravelStyleForm, BudgetForm, DurationForm, LanguageForm
)

def auth_view(request):
    # Instantiate both forms; bind POST data if present
    login_form    = LoginForm(request, data=request.POST or None)
    register_form = RegisterForm(request.POST or None)

    if request.method == 'POST':
        # Determine which form was submitted
        form_type = request.POST.get('form_type')
        if form_type == 'login':
            # LOGIN flow
            if login_form.is_valid():
                # Log the user in and redirect
                auth_login(request, login_form.get_user())
                messages.success(request, f"Welcome back, {login_form.get_user().username}!")
                return redirect('dashboard')
            else:
                # Show an error and fall through to re-render
                messages.error(request, "Invalid email or password. Please try again.")
        else:
            # REGISTRATION flow
            if register_form.is_valid():
                # Create the new user, log them in, and redirect
                user = register_form.save()
                auth_login(request, user)
                messages.success(request, f"Thanks for signing up, {user.username}!")
                return redirect('dashboard')
            else:
                # Show an error and fall through to re-render
                messages.error(request, "Please correct the errors below and resubmit.")

    # GET requests or invalid POST just re-render the combined auth page
    return render(request, 'auth.html', {
        'login_form':    login_form,
        'register_form': register_form,
    })


def logout_view(request):
    logout(request)
    messages.success(request, "You’ve been signed out.")
    return redirect('landing')


def landing(request):
    return render(request, 'landing.html')

def onboarding(request):
    # A dummy onboarding view to be enhanced later.
    return render(request, 'onboarding.html')

@login_required
def dashboard(request):
    recommendations = TripPackage.objects.all()[:6]  # placeholder
    # Only “draft” trips: let user continue building
    current_trip = Trip.objects.filter(user=request.user, status='draft').first()
    upcoming_trips = Trip.objects.filter(user=request.user, status='booked')
    saved_itineraries = Trip.objects.filter(user=request.user).exclude(status='draft')
    return render(request, 'dashboard.html', {
      'recommendations': recommendations,
      'upcoming_trips': upcoming_trips,
      'saved_itineraries': saved_itineraries,
      'current_trip': current_trip,
    })

@login_required
def dashboard_view(request):
    user = request.user
    # Example: upcoming trips (you’ll need a model for bookings/itineraries)
    upcoming = user.bookings.filter(date__gte=timezone.now()).order_by('date')  
    saved_itineraries = user.itineraries.all()   # if you have a related model
    return render(request, 'dashboard.html', {
        'upcoming': upcoming,
        'saved_itineraries': saved_itineraries,
    })

@login_required
def profile_view(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated!")
            return redirect('profile')
    else:
        form = ProfileForm(instance=user)

    return render(request, 'profile.html', { 'form': form })

@login_required
def profile(request):
    return render(request, 'profile.html')

# Define the sequence of steps
FORMS = [
    ("style",    TravelStyleForm),
    ("budget",   BudgetForm),
    ("duration", DurationForm),
    ("language", LanguageForm),
]

# Map each step to its template
TEMPLATES = {
    "style":    "onboarding/style.html",
    "budget":   "onboarding/budget.html",
    "duration": "onboarding/duration.html",
    "language": "onboarding/language.html",
}

class OnboardingWizard(SessionWizardView):
    """
    Multi-step onboarding wizard using django-formtools.
    Saves preferences to the user's profile at the end.
    """
    form_list = FORMS

    def get_template_names(self):
        """Return the template for the current step."""
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        # Aggregate cleaned data from all steps
        data = {}
        for form in form_list:
            data.update(form.cleaned_data)

        # Save to the CustomUser profile (adjust if your relation differs)
        user = self.request.user
        user.travel_style = data.get('travel_style', '')
        # Assuming you added budget, duration, languages fields to your CustomUser
        user.budget = data.get('budget', '')
        user.duration = data.get('duration', '')
        user.languages = ",".join(data.get('languages', []))
        user.save()

        # Redirect to dashboard when done
        return redirect('dashboard')

def contact_view(request):
    # If the form is submitted...
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            full_message = f"Message from {name} <{email}>:\n\n{message}"
            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            # Redirect to a thank-you page or back to contact
            return redirect('contact_success')
    else:
        # On GET, show an empty form
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form
    })

def destinations(request):
    # Dummy data – you can replace with real QuerySet later
    destinations = [
        {
            'id': 1,
            'name': 'Shah Faisal Mosque, Islamabad',
            'short_description': 'Iconic white-marble mosque with sweeping mountain backdrop.',
            'image': '/static/images/shah_faisal.jpg',
        },
        {
            'id': 2,
            'name': 'Nathia Gali, Kashmir',
            'short_description': 'Pine‑clad hill station with misty forest trails and cool climate.',
            'image': '/static/images/nathia_gali.jpg',
        },
        {
            'id': 3,
            'name': 'Lahore Fort, Punjab',
            'short_description': '16th‑century citadel in the old walled city of Lahore.',
            'image': '/static/images/lahore_fort.jpg',
        },
    ]
    return render(request, 'destinations.html', {'destinations': destinations})

def destination_detail(request, id):
    # In real life, query your model; here we echo our dummy list above
    all_dests = {
        1: {
            'name': 'Shah Faisal Mosque, Islamabad',
            'image': '/static/images/shah_faisal.jpg',
            'long_description': 'Built in 1986, one of the largest mosques in the world...',
            'highlights': [
                'Stunning mountain backdrop',
                'Unique geometric architecture',
                'Evening sound-and-light show',
            ],
        },
        # ... similarly for id 2 and 3 ...
    }
    dest = all_dests.get(id)
    if not dest:
        return redirect('destinations')
    return render(request, 'destination_detail.html', {'dest': dest})

def tour_packages(request):
    # Dummy data for demonstration
    sample = [
        {'id': 1, 'title': 'Kashmir Valley Escape', 'location': 'Azad Kashmir', 
         'duration': 5, 'price': 350, 'image_url': None},
        {'id': 2, 'title': 'Northern Pakistan Adventure', 'location': 'Gilgit‑Baltistan', 
         'duration': 7, 'price': 700, 'image_url': None},
        {'id': 3, 'title': 'Hunza & Skardu Highlights', 'location': 'Hunza', 
         'duration': 6, 'price': 600, 'image_url': None},
        # Add more dummy packages as needed
    ]
    return render(request, 'tour_packages.html', {
        'packages': sample
    })

@login_required
def package_detail(request, pk):
    pkg = get_object_or_404(TripPackage, pk=pk)
    # If user clicks “Add to Itinerary”
    if request.method == 'POST':
        # Grab or create an “in-progress” itinerary
        itin, created = request.user.itinerary_set.get_or_create(name="My Trip", defaults={})
        itin.packages.add(pkg)
        return redirect('itinerary_detail', itin.id)

    return render(request, 'package_detail.html', {'pkg': pkg})

@login_required
def add_to_itinerary(request, pk):
    pkg = get_object_or_404(TripPackage, pk=pk)
    trip, created = Trip.objects.get_or_create(user=request.user, status='draft')
    trip.packages.add(pkg)
    messages.success(request, f'"{pkg.title}" added to your itinerary.')
    return redirect('package_detail', pk=pk)


def tour_packages(request):
    sample = [
        {
            'id': 1,
            'title': 'Kashmir Valley Getaway',
            'location': 'Neelum Valley, Kashmir',
            'short_description': '5 nights of scenic beauty and houseboat stays.',
            'duration': 5,
            'price': 499,
            'image_url': None
        },
        {
            'id': 2,
            'title': 'Hunza Adventure Trek',
            'location': 'Hunza, Pakistan',
            'short_description': '7-day trek through the Karakoram mountains.',
            'duration': 7,
            'price': 799,
            'image_url': 'https://example.com/hunza.jpg'
        },
        {
            'id': 3,
            'title': 'Lahore Heritage Tour',
            'location': 'Lahore, Pakistan',
            'short_description': 'Explore Mughal architecture and bazaars.',
            'duration': 3,
            'price': 299,
            'image_url': None
        },
    ]
    return render(request, 'tour_packages.html', {
        'packages': sample
    })


def local_businesses(request):
    # You might filter by travel_style or other criteria later
    businesses = LocalBusiness.objects.all()
    return render(request, 'local_businesses.html', {
        'businesses': businesses
    })


def faq(request):
    # Dummy FAQ entries, highlighting Pakistan/Kashmir
    faqs = [
        {
            'question': 'What is the best time to visit Kashmir?',
            'answer': 'The ideal season is from March to October when the weather is mild and the valleys bloom with flowers.'
        },
        {
            'question': 'How can I book a houseboat stay on Dal Lake?',
            'answer': 'Navigate to our “Tour Packages” page and select the “Kashmir Houseboat Experience” package to reserve your room.'
        },
        {
            'question': 'Are there eco‑friendly treks in Hunza Valley?',
            'answer': 'Yes—Tourista partners with local eco‑lodges and guides who practice low‑impact camping in the Nagar region.'
        },
        {
            'question': 'Do I need a permit for Neelum Valley?',
            'answer': 'No special permits are required for Neelum Valley; however, always carry your ID and follow local guidelines.'
        },
    ]
    return render(request, 'faq.html', {'faqs': faqs})

def trip_planner(request):
    real_pkgs = TripPackage.objects.all()
    packages = []
    fallback = {
        'Hunza Valley Explorer': 'images/hunza.jpg',
        'Neelum Valley Retreat':   'images/neelum.jpg',
        'Murree & Ayubia Getaway': 'images/murree.jpg',
    }
    for pkg in real_pkgs:
        if pkg.image:
            img_url = pkg.image.url
        else:
            img_url = static(fallback.get(pkg.title, 'images/dummy_destination.jpg'))
        packages.append({
            'pk':                pkg.pk,
            'title':             pkg.title,
            'short_description': pkg.short_description,
            'image_url':         img_url,
        })

    return render(request, 'trip_planner.html', {'packages': packages})


def about(request):
    team = [
        {
            'name': 'Jane Khan',
            'role': 'Co-Founder & CEO',
            'photo': '/static/images/team_member1.jpg',
            'linkedin': '#',
        },
        {
            'name': 'Omar Ali',
            'role': 'CTO',
            'photo': '/static/images/team_member2.jpg',
            'linkedin': '#',
        },
        {
            'name': 'Ayesha Mir',
            'role': 'Head of Marketing',
            'photo': '/static/images/team_member3.jpg',
            'linkedin': '#',
        },
        {
            'name': 'Zain Ahmed',
            'role': 'Lead Developer',
            'photo': '/static/images/team_member4.jpg',
            'linkedin': '#',
        },
    ]
    context = {
        'team': team,
        'mission': 'Empower travelers and uplift local communities with AI-driven, sustainable tourism.',
        'vision': 'Become the world’s most trusted eco-friendly travel companion.',
        'values': [
            'Innovation',
            'Sustainability',
            'Authenticity',
            'Community',
        ]
    }
    return render(request, 'about.html', context)


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            full_message = f"From {cd['name']} <{cd['email']}>:\n\n{cd['message']}"
            send_mail(
                cd['subject'],
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                fail_silently=False
            )
            return redirect('contact')  # or show a “thank you” message
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def business_detail(request, pk):
    # Fetch or 404
    biz = get_object_or_404(LocalBusiness, pk=pk)
    # Dummy reviews for demo
    reviews = [
        {'author': 'Ali R.', 'rating': 5, 'text': 'Fantastic service and atmosphere!'},
        {'author': 'Sara K.', 'rating': 4, 'text': 'Great location, friendly staff.'},
    ]
    return render(request, 'business_detail.html', {
        'biz': biz,
        'reviews': reviews,
    })


def destination_detail(request, pk):
    pkg = get_object_or_404(TripPackage, pk=pk)
    return render(request, 'destination_detail.html', {'package': pkg})

@login_required
def itinerary_detail(request, pk):
    itin = get_object_or_404(Itinerary, pk=pk, user=request.user)
    return render(request, 'itinerary_detail.html', {'itin': itin})