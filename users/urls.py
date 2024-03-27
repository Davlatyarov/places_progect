from django.urls import path
from . import views
from .views import LoginView, LogoutView
app_name = 'users'


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileUpdateView.as_view(), name='profile'),
    path('profile_new/', views.ProfileView.as_view(), name='profile_new'),

    path('api/login/', LoginView.as_view(), name='api-login'),
    path('api/logout/', LogoutView.as_view(), name='api-logout'),
    
]
