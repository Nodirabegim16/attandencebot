from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=200)

class Student(models.Model):
    fullname = models.CharField(max_length=10)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10)

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    is_come = models.BooleanField(default=True)
    day = models.DateTimeField()


