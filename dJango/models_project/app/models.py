from django.db import models

# Create your models here.
class Employees(models.Model): # create table table_name()
    # id int
    # age int
    # name varchar(50) not null
    # cln_name = dataype(contraints)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.CharField(max_length=50)
    dept = models.CharField(max_length=20)

    def __str__(self):
        return self.name
