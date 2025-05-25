from django.db import models

class Info(models.Model):
    Name= models.CharField(max_length=50)
    Age= models.IntegerField()
    Gender= models.CharField(max_length=20) 
    Job= models.CharField(max_length=100)
    Hobbies= models.TextField()

    def __str__(self):
        return self.name
