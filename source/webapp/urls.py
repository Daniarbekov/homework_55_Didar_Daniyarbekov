
from django.urls import path
from webapp.views.base import index_view
from webapp.views.task import task_create_view, detail_view



urlpatterns= [
    path("", index_view, name='index'),
    path("task_create", task_create_view, name='create_task'),
    path('task_detail/<int:pk>',detail_view, name='detail_task')
]