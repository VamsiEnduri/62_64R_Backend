from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age=models.IntegerField()
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=14)

    def __str__(self):
        return self.name