from django.db import models

class Post(models.Model):
    title = models.CharField(verbose_name='Назва', max_length=100)
    content = models.TextField(verbose_name='Тип контенту')
    published_date = models.DateTimeField()
