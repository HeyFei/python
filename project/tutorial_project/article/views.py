from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Article
from django.views.generic import (
    DetailView,
)


def index(request):
    context = {
        'articles': Article.objects.all()
    }
    return render(request, 'article/index.html', context)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/detail.html'
