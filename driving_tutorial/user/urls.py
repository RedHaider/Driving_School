from django.urls import path
from .views import home, about, contact ,courses, appointment, dashboard, logout_view
from . import views

urlpatterns = [
    path('', home, name='home'),  # URL for the home view
    path('about/', about, name='about'),
    path('courses/', courses, name='courses'),
    path('appointment/', appointment, name='appointment'),
    path('contact', contact, name='contact'),
    path('dashboard/', dashboard, name='dashboard'),
    path('registration/', views.UserRegistrationView.as_view(), name='register' ),
    path('login/', views.LoginView.as_view(), name='login'),
     path('logout/', logout_view, name='logout'),
    
]
