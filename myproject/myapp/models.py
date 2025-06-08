from django.db import models
from django.core import validators
class Info(models.Model):
    Name= models.CharField(max_length=50)
    Age= models.IntegerField()
    Gender= models.CharField(max_length=20) 
    Job= models.CharField(max_length=100)
    Hobbies= models.TextField()

    def __str__(self):
        return self.Name
    
class Book(models.Model):
    Title= models.CharField(max_length=200)
    Author= models.CharField()
    Description= models.TextField()
    Price= models.IntegerField(validators=[validators.MaxValueValidator(1000000),validators.MinValueValidator(1000)])
    Created_at =models.DateTimeField()

    def __str__(self):
        return self.Title