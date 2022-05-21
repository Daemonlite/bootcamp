from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    COURSES=(
        ('python','python'),
        ('c++','c++'),
        ('javascript','javascript'),
        ('swift','swift'),
        ('html','html'),
        ('css','css'),
        ('Ruby','Ruby'),
        ('c#','c#'),
        ('c#','c#'),
    )
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=250)
    age = models.IntegerField(default=0)
    email = models.EmailField()
    course = models.CharField(choices=COURSES, max_length=200)

    def __str__(self):
        return self.full_name

class Tutor(models.Model):
    COURSES=(
        ('python','python'),
        ('c++','c++'),
        ('javascript','javascript'),
        ('swift','swift'),
        ('html','html'),
        ('css','css'),
        ('Ruby','Ruby'),
        ('c#','c#'),
        ('c#','c#'),
    )
    full_name = models.CharField(max_length=250)
    age = models.IntegerField(default=0)
    cv = models.FileField(upload_to='files')
    email = models.EmailField()
    course = models.CharField(choices=COURSES, max_length=200)

    def __str__(self):
        return self.full_name


class Newsletter(models.Model):
    email = models.EmailField()


