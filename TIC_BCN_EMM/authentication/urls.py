from django.urls import path
from . import views

urlpatterns = [
    # Rutes per al login sense sessió
    path('login_without_session/', views.login_without_session, name='login_without_session'),
    path('home_without_session/', views.home_without_session, name='home_without_session'),
    
    # Rutes per al login amb sessió
    path('login_with_session/', views.login_with_session, name='login_with_session'),
    path('home_with_session/', views.home_with_session, name='home_with_session'),
    
    # Ruta per fer logout
    path('logout/', views.logout_view, name='logout'),
]