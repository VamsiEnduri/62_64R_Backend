from django.db import models

# Create your models here.

class patients(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    disease_type=models.CharField(max_length=50,default="N/A")

    def __str__(self):
        return self.name

