from django.urls import path
from . import views
urlpatterns = [
    path("task/", views.TaskAPIView.as_view(), name = 'task-list')
]