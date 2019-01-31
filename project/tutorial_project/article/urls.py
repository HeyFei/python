from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
)
from . import views


urlpatterns = [
    path('', views.index, name='article-index'),
    #path('', ArticleListView.as_view(), name='article-index'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
]
