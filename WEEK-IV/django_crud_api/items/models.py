from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    grade = models.CharField(max_length=10, default="A")

    def __str__(self):
        return self.name
