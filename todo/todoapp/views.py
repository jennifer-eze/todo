from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

class TodoList(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        todo_data = TodoSerializer(todos, many = True)
        return Response(todo_data.data)

    def post(self, request):
        todo = TodoSerializer(data=request.data)
        if todo.is_valid():
            todo.save()
        return Response(todo.data)

    def delete(self, request):
        Todo.objects.all().delete()
        return Response(None)

class TodoOne(APIView):
    pass

