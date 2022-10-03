from django.core.exceptions import ValidationError
from django import forms
from django.forms import widgets
from webapp.models import Task

class TaskForm(forms.Form):

    title = forms.CharField(max_length=100, label='Описание',required=False)
    date = forms.DateField(label='Дата выполения',widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    status = forms.ChoiceField(label='Статус',widget=forms.Select, choices=Task.CHOICES)
    description = forms.CharField(max_length=600, label='Подробное описание', widget=widgets.Textarea,required=False)
    
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise ValidationError('Поле не заполнено')
        elif len(title) > 200:
            raise ValidationError('Должно быть меньше 100 символов')
        return title 
    
    def len_desc(self):
        description = self.cleaned_data.get('description')
        if len(description) > 600:
            raise ValidationError('Должно быть меньше 600 символов')    