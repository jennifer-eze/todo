from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

class TodoList(APIView):
    def get(self, request):
        return Response(None)
        
    def post(self, request):
        todo = TodoSerializer(request.data)
        return Response(todo.data)

class TodoOne(APIView):
    pass

