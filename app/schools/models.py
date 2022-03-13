from django.db import models


class School(models.Model):
    name = models.CharField(max_length=20)
    max_student = models.PositiveIntegerField()


class Student(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    student_id = models.CharField(max_length=20)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

