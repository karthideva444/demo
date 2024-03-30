# from django.shortcuts import render
# from .models import Student
# from .serializers import StudentSerializers
# from rest_framework.renderers import JSONRenderer
# from django.http import HttpResponse
# from rest_framework.parsers import JSONParser
# import io
# from django.views.decorators.csrf import csrf_exempt


# def student_details(request):
#     stu = Student.objects.get(roll=2)
#     serializer = StudentSerializers(stu)
#     json_data = JSONRenderer.render(serializer.data)
#     return HttpResponse(json_data,content_type='application/json')


# @csrf_exempt  
# def student_create(request):
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser.parse(stream)
#         serializer = StudentSerializers(data=python_data)
#         if serializer.is_valid:
#             serializer.save()
#             res = {'msg':'data created successfully'}
#             json_data = JSONRenderer.render(res)
#             return HttpResponse(json_data,content_type='application/json')
#         return HttpResponse(JSONRenderer.render(serializer.errors),content_type='application/json')
    
    # if request.method == 'PUT':
    #     json_data = request.body
    #     stream = io.BytesIO(json_data)
    #     python_data = JSONParser.parse(stream)
    #     id = python_data.get(id)
    #     serializer = StudentSerializers('id',None)
    #     if serializer.is_valid:



     
