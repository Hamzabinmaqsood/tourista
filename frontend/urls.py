from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from .api import nearby_businesses

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name='landing'),
    path('auth/', views.auth_view, name='auth'),   # Combined page
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('onboarding/', views.onboarding, name='onboarding'),
    path('profile/', views.profile, name='profile'),
    path('logout/', LogoutView.as_view(next_page='landing'), name='logout'),
    path('api/nearby-businesses/', nearby_businesses, name='nearby_businesses'),
]
