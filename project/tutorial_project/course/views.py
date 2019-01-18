from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Course


def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'course/index.html', context)
