from django.urls import path
from . import views

urlpatterns = [
    path('reg/',views.registerView, name='register_urls'),
    path('',views.loginView, name='login_urls'),
    path('lot/',views.logoutView, name='logout_urls')
]