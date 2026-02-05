from django.db import models

# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length=5)
    age = models.IntegerField()
    email =models.EmailField(unique=True) 
    dept = models.CharField(max_length=50)

    def __str__(self):
        return self.name