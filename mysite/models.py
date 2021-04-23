from django.db import models

# Create your models here.


class Student(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.email