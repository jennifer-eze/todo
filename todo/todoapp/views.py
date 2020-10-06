from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
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
            todo_item = todo.save()
            todo_item.completed = False
            todo_item.url = reverse('todo_one', args=[todo_item.id], request=request)
            todo_item.save()
        return Response(todo.data)

    def delete(self, request):
        Todo.objects.all().delete()
        return Response(None)

class TodoOne(APIView):
    def get(self, request, todo_id):
        todo = Todo.objects.get(pk=todo_id)

        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def patch(self, request, todo_id):
        todo = Todo.objects.get(pk=todo_id)
        serializer = TodoSerializer(data=request.data, instance=todo, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, todo_id):
        todo = Todo.objects.get(pk=todo_id)
        todo.delete()
        return Response(None)