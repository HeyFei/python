from django.urls import path
from .views import (
    ArticleDetailView,
)
from . import views


urlpatterns = [
    path('', views.index, name='article-index'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
]
