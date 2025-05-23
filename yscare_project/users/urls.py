from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('main/', views.main_view, name='main'),
    path('health_info/', views.health_info_view, name='health_info'),
]