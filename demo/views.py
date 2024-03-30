
# Model and Serializers
from .models import Student
from .serializers import StudentSerializer
import io

# Django
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

#rest_framework
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data created successfully'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        return HttpResponse (JSONRenderer().render(serializer.errors),content_type='application/json')
    
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)      
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu,data=python_data)
            if serializer.is_valid():
                serializer.save()
                res = {'msg':'data updated successfully'}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data,content_type='application/json')
            res = {'msg':'data not valid'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        res = {'msg':'id is not valid'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        if id is not None:   
            try:          
                stu = Student.objects.get(id=id)
                stu.delete()
                res = {'msg':'data deleted successfully'}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data,content_type='application/json')
            except Student.DoesNotExist:
                res = {'msg':'invalid id'}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data,content_type='application/json')
        res = {'msg':"id is NONE"}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')
        


@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data created successfully...'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        return HttpResponse(JSONRenderer().render(serializer.errors),content_type='application/json')


