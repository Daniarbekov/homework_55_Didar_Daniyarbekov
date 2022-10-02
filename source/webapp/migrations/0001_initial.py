# Generated by Django 4.1.1 on 2022-10-02 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Описание')),
                ('status', models.CharField(default='new', max_length=50, verbose_name='Статус')),
                ('date', models.DateField(blank=True, max_length=50, null=True, verbose_name='Дата выполнения')),
                ('description', models.TextField(blank=True, max_length=400, null=True, verbose_name='Подробное описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
        ),
    ]