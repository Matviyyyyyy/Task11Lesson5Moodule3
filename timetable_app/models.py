from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()

class Teacher(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)

class Class(models.Model):
    name = models.CharField(max_length=250, unique=True)
    year = models.IntegerField()

class Student(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    class_s = models.ForeignKey(Class, on_delete=models.DO_NOTHING)

class Schedule(models.Model):
    day_of_week = models.CharField(max_length=100)
    start_time = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    class_s = models.ForeignKey(Class, on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    mark = models.IntegerField(validators=[MaxValueValidator(12)])