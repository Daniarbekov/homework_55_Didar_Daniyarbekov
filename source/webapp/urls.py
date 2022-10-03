
from django.urls import path
from webapp.views.base import index_view
from webapp.views.task import task_create_view



urlpatterns= [
    path("", index_view, name='index'),
    path("task_create", task_create_view, name='create_task')
]