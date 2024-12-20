from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404
from .models import *


def home(request: WSGIRequest):
    lesson = Lesson.objects.all()
    context = {
        "lesson": lesson,
        'title': 'Barcha kurs hamda darslar'
    }
    return render(request, "index.html", context)


def lessons_by_courses(request: WSGIRequest, course_id):
    course = get_object_or_404(Course, id=course_id)
    lesson = Lesson.objects.filter(course_id=course_id)

    context = {
        'courses': [course],
        'lessons': lesson,
    }

    return render(request, 'index.html', context)


def lessons(request: WSGIRequest, course_id):
    lessons = Lesson.objects.filter(course_id=course_id)
    course = Course.objects.get(pk=course_id)
    context = {
        'lessons': lessons,
        'title': f'{course.name}: barcha darslar '
    }
    return render(request, 'index.html', context)


def course(request: WSGIRequest, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)

    context = {
        'lesson': lesson,
    }

    return render(request, 'detail.html', context)
