from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task
from .decorators import custom_decorator

class TaskAPIView(APIView):
    """
    A simple APIView for creating contact entires.
    """

    @custom_decorator
    def get(self, request):
        items = Task.objects.all()
        data = [{"task": item.task, "due_date": item.due_date} for item in items]

        return Response(data, status=status.HTTP_200_OK)

    @custom_decorator
    def post(self, request):
        task = request.data.get("task")
        due_date = request.data.get("due_date")
        item = Task.objects.create(task=task, due_date=due_date)
        return Response({"id": item.id, "task": item.task, "due_date": item.due_date}, status=status.HTTP_201_CREATED)
