from django.urls import path
from .views import (
    CourseDetailView,
)
from . import views


urlpatterns = [
    path('', views.index, name='course-index'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    #path('detail', views.detail, name='course-detail'),
]
