from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

from .views import PasswordsChangeView

app_name = 'accounts'

urlpatterns = [
    path('register/', views.MyRegisterFormView.as_view(), name='register'),
    path('<int:pk>/', views.UserProfileView.as_view(), name='profile'),
    path('login/', views.user_login, name='login'),
    path("logout/", views.logout, name="logout"),
    path('edit_profile/', views.UserEditFormView.as_view(), name='edit_profile'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='accounts/password.html')),
    path('password/', PasswordsChangeView.as_view(template_name='accounts/password.html')),
    path('password_success', views.password_success, name='password_success'),
    path('<int:pk>/profile/', views.UserProfileView.as_view(), name='profile'),
    path('<int:pk>/edit_profile_page', views.EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page', views.CreateProfilePageView.as_view(), name='create_profile_page'),
]