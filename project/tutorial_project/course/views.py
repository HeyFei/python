from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Course
from django.views.generic import (
    DetailView,
)


def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'course/index.html', context)


def detail(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'course/detail.html', context)


class CourseDetailView(DetailView):
    model = Course
    template_name = 'course/detail.html'
