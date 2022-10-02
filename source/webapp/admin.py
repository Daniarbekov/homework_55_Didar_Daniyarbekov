from django.contrib import admin
from webapp.models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id','title','description','status','date')
    list_filter = ('id','title','description','status','date')
    search_fields = ['status']
    fields = ('id','title','description','status','date')
    readonly_fields = ('id','date')

admin.site.register(Task, TaskAdmin)