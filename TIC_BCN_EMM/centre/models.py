from django.db import models

# Create your models here.
class student(models.Model):
    id = models.IntegerField
    first_name = models.CharField(max_length=50)
    last_name_1 = models.CharField(max_length=50)
    last_name_2 = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    enrolled_modules = models.TextField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name_1} {self.last_name_2}"

class teacher(models.Model):
    id = models.IntegerField
    first_name = models.TextField()
    last_name_1 = models.TextField()
    last_name_2 = models.TextField()
    email = models.TextField()
    course = models.TextField()
    tutor = models.BooleanField(default=False)
    teaching_modules = models.TextField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name_1} {self.last_name_2}"
