from django.db import models

# Create your models here.
class Employees(models.Model):
    name  = models.CharField(max_length=50)
    age = models.IntegerField()
    email  = models.CharField(max_length=50)
    dept = models.CharField(max_length=50)
    sal = models.IntegerField()

    def __str__(self):
        return self.name