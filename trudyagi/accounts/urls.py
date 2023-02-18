from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'accounts'

urlpatterns = [
    path('registration/', views.RegisterView.as_view(), name="register"),
    path('login/', views.LoginUserView.as_view(), name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('profile/<str:username>', views.profile_view, name='profile'),
    path('activation/user_key/<str:sign>', views.activation_user_view, name='activation_page'),
    path('activation/warning', views.activation_warning_view, name='activation_warning')
]
