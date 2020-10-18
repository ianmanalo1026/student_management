from django.db import models
from django.db.models.fields import PositiveSmallIntegerField


YEAR_CHOICES = [
        ("1st","First"),
        ("2nd","Second"),
        ("3rd","Third"),
        ("4th","Fourth"), 
]

class Course(models.Model):
    name = models.CharField(max_length=500)
    code = models.CharField(max_length=10)
    description = models.TextField()
    
    
    def __str__(self):
        return self.code
    

class Subject(models.Model):
    subject = models.CharField(max_length=250)
    subject_code = models.CharField(max_length=50)
    subject_year = models.CharField(max_length=50, choices=YEAR_CHOICES, default="1st",)
    subject_unit = PositiveSmallIntegerField()
    subject_description = models.TextField()
    subject_course = models.OneToOneField(Course,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.subject_code
    

class Student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    birthday = models.DateField(auto_now_add=False)
    student_course = models.OneToOneField(Course, on_delete=models.CASCADE)

    
    
    def __str__(self):
        return self.lastname + ", " + self.firstname