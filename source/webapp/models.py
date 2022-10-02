from django.db import models

# Create your models here.
class Task(models.Model):
    CHOICES = [('new', 'Новая'),('in process', 'в процессе'),('done','сделано')]

    title = models.CharField(verbose_name='Описание', max_length=200, blank=False, null=False)
    status = models.CharField(verbose_name='Статус',max_length=50, default='new', null=False)
    date = models.DateField(verbose_name='Дата выполнения', max_length=50, null=True, blank=True)
    description = models.TextField(verbose_name='Подробное описание', max_length=400,null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    

    def __str__(self) -> str:
        return f"{self.title} - {self.status} - {self.date}"
    
