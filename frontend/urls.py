from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView 
from . import views
from .api import nearby_businesses
from .views import OnboardingWizard
from .views import auth_view, logout_view, landing, trip_planner, package_detail, dashboard, profile, contact_view, itinerary_detail
from django.conf import settings
from django.conf.urls.static import static
from .views import package_detail, add_to_itinerary

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', views.landing, name='landing'),
    path('trip-planner/', views.trip_planner, name='trip_planner'),
    path('packages/<int:pk>/', views.package_detail, name='package_detail'),
    path('auth/', auth_view, name='auth'),
    path('logout/', LogoutView.as_view(next_page='landing'), name='logout'),
    path('login/', views.auth_view, name='login'),
    path('register/', views.auth_view, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('onboarding/', OnboardingWizard.as_view(), name='onboarding'),
    path('profile/', views.profile, name='profile'),
    path('api/nearby-businesses/', nearby_businesses, name='nearby_businesses'),
    path('about/', TemplateView.as_view(template_name="about.html"), name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('destinations/', views.destinations, name='destinations'),
    path('destinations/<int:id>/', views.destination_detail, name='destination_detail'),
    path('destinations/<int:pk>/', views.destination_detail, name='destination_detail'),
    path('packages/', views.tour_packages, name='tour_packages'),
    path('destinations/<int:pk>/', views.destination_detail, name='destination_detail'),
    path('businesses/', views.local_businesses, name='local_businesses'),
    path('businesses/<int:pk>/', views.business_detail, name='business_detail'),
    path('packages/<int:pk>/', views.package_detail, name='package_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path(
      'contact/success/',
      TemplateView.as_view(template_name="contact_success.html"),
      name='contact_success'
    ),
    path('packages/', views.tour_packages, name='tour_packages'),
    path('packages/<int:pk>/', views.package_detail, name='package_detail'),
    path('faq/', views.faq, name='faq'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('itinerary/<int:pk>/', itinerary_detail, name='itinerary_detail'),
]


# Serve MEDIA files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
