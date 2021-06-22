from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_token
from rest_framework.parsers import JSONParser
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status   
from .models import UserTwitter, AdditionalData
from .serializers import UserSerializer, AditionalDataSerializer
import hashlib

# Create your views here.
@api_view(['GET', 'POST'])
def imageLoadUser(request, id):
    try:
        user = UserTwitter.objects.get(id=id)
        files = request.FILES
        user.photo = files['imagen']
        user.save()
        return Response({'response': "ok"})
    except UserTwitter.DoesNotExist:
        return Response({"error": "This user not exist"}, status=404)

class UserApi(APIView):

    def get(self, request, format=None):
        users = UserTwitter.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        request.data['password'] = hashlib.sha256(request.data['password'].encode()).hexdigest()
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

class UserApiDetails(APIView):

    def __getuser__(self, id):
        user = UserTwitter.objects.get(id=id)
        return user

    def get(self, request, id, format=None):
        try:
            user = self.__getuser__(id)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except UserTwitter.DoesNotExist:
            return Response({"error": "This user not exist"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id, format=None):
        try:
            user = self.__getuser__(id)

            serializer = UserSerializer(user)
            return Response(serializer.data)
        except UserTwitter.DoesNotExist:
            return Response({"error": "This user not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as error:
            return Response({"error": "A error has been ocurred"}, status=status.HTTP_400_BAD_REQUEST)


    


