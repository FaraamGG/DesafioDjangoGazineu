from django.db.models import Q
from django.http import Http404
from django.shortcuts import render

from .models import Course


def home(request):
    # Queryset de todos os cursos publicados listados por ordem de id decrescente
    courses = Course.objects.filter(is_published=True).order_by('-id')
    return render(request, 'institute/pages/home.html', context={
        'courses': courses,
    })


def course(request, course_id):
    # Queryset dos cursos filtrados por id, first para selecionar o objeto
    course = Course.objects.filter(id=course_id).first()
    return render(request, 'institute/pages/course-view.html', context={
        'course': course,
        'is_course': True,
    })


def teacher(request, teacher_id):

    # Queryset dos cursos filtrado pelo id da foreign key 'teacher' ordenado por id decrescente
    courses = Course.objects.filter(
        teacher__id=teacher_id, is_published=True).order_by('-id')

    return render(request, 'institute/pages/teacher.html', context={
        'courses': courses,
        'teacher': courses[0].teacher.name
    })


def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404

    # Queryset dos cursos filtrados por título ou descrição ordenado por id decrescente
    # A cláusula where utiliza do LIKE para encontrar título ou descrição semelhantes ao termo de pesquisa
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
