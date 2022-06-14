from django.db.models import Q
from django.http import Http404
from django.shortcuts import render

from .models import Course


# Create your views here.
def home(request):
    courses = Course.objects.filter(is_published=True).order_by('-id')
    return render(request, 'institute/pages/home.html', context={
        'courses': courses,
    })


def course(request, course_id):
    course = Course.objects.filter(id=course_id).first()
    return render(request, 'institute/pages/course-view.html', context={
        'course': course,
        'is_course': True,
    })


def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404

    courses = Course.objects.filter(
        Q(
            Q(title__icontains=search_term) | Q(
                description__icontains=search_term)
        ),
        is_published=True
    ).order_by('-id')

    return render(request, 'institute/pages/search.html', {
        'page_title': f'Search for "{search_term}" | ',
        'search_term': search_term,
        'courses': courses
    })
