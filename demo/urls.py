from django.urls import path
from demo.views import student_api,student_create,hello


urlpatterns = [
    path('student_api/',student_api,name='student'),
    path('create_student/',student_create,name='createstudent'),
    path('',hello,name='hello')
]