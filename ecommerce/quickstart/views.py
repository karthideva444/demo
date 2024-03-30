from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse


from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from .serializers import GroupSerializer, UserSerializer
from .models import UserProfile

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class customerview(APIView):
    def post(self,request,*args,**kwargs):
            name = request.data.get("name")
            email = request.data.get("email")
            phone = request.data.get("phonenumber")
            age = request.data.get("age")
            Dob = request.data.get("Dob")
            password = request.data.get("Password")
            try:
                obj = UserProfile.objects.create(
                     name=name,
                     email=email,
                     phone=phone,
                     age=age,
                     Dob=Dob,
                     password=password)
                return Response("Data Stored Successfully...",status=status.HTTP_201_CREATED)
            except Exception as e:
                 return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
            
    def get(self,request,*args,**kwargs):
         try:
            id = str(kwargs["pk"])
            res = UserProfile.objects.get(pk=id)
            data = {"name":res.name,"email":res.email}
            return Response(data,status=status.HTTP_200_OK)
         except Exception as e:
              return Response(str(e),status=status.HTTP_400_BAD_REQUEST) 
            
         
         
                    

                
            
            
            

                


        