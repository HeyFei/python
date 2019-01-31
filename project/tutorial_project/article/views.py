from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

# Create your views here.
from .models import Article
from django.views.generic import (
    ListView,
    DetailView,
)


def index(request):
    # context = {
    #     'articles': Article.objects.all()
    # }
    # return render(request, 'article/index.html', context)

    article_list = Article.objects.all().order_by('-date_posted')
    paginator = Paginator(article_list, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'article/index.html', {'articles': articles})


class ArticleListView(ListView):
    model = Article
    template_name = 'article/index.html'
    context_object_name = 'articles'
    ordering = ['-date_posted']
    paginate_by = 1


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/detail.html'
