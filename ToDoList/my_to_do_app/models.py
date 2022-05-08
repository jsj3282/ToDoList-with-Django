from django.db import models

# Create your models here.
class ToDo(models.Model):
    content = models.CharField(max_length=255, default="")
    isDone = models.BooleanField(default=False)
