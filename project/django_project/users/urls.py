from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('register/', views.reg, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    #path(r'^go-to-django/$', RedirectView.as_view(url='http://djangoproject.com')),
    path('redirect/', RedirectView.as_view(url='http://www.google.com'), name='go-to-google')
]
