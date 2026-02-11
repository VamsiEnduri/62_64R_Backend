from django.db import models

# Create your models here.
class Doctor(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    phNum=models.CharField(max_length=15)
    password=models.CharField(max_length=14)
    c_password=models.CharField(max_length=14)
    role=models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    phNum=models.CharField(max_length=15)
    password=models.CharField(max_length=14)
    c_password=models.CharField(max_length=14)
    role=models.CharField(max_length=15)

    def __str__(self):
        return self.name
