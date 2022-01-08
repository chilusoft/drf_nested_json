from django.db import models

# Create your models here.

class StudentData(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name

class StudentResult(models.Model):

    student = models.ForeignKey(StudentData, on_delete=models.CASCADE, related_name='student')
    math = models.IntegerField()
    english = models.IntegerField()
    history = models.IntegerField()
    science = models.IntegerField()

    def __str__(self):
        return str(self.student)
