from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
    
class Student_class(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
       
class Preson(models.Model):
    fname = models.CharField(max_length=250)
    lname = models.CharField(max_length=250)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)
    student_class = models.ForeignKey(Student_class,on_delete=models.CASCADE)
    

