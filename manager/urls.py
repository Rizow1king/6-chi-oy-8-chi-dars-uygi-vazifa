from .views import *
from django.urls import path

urlpatterns = [
    path("", home, name="home"),
    path("courses/<int:course_id>/", lessons_by_courses, name='course'),
    path("lesson/<int:lesson_id>/", lessons, name='lesson')
]
