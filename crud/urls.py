from django.contrib import admin
from django.urls import path
from .views import student_details,student_create

urlpatterns = [
    path('/', admin.site.urls),
    # path('',include('ecommerce.quickstart.urls'))
    path('students/',view=student_details,name='student'),
    # path('createstudent/',view=student_create,name='createstudent')
    
]