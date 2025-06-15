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
    
class Keyboard(models.Model):
    Name= models.CharField(max_length=75)
    Image=models.ImageField(upload_to='images',default='bad_sign.png')
    Price= models.IntegerField(validators=[validators.MaxValueValidator(3000000),validators.MinValueValidator(1000)])
    Short_Description= models.TextField(max_length=300)
    Material=models.CharField(max_length=100)
    Place_of_Origin=models.CharField(max_length=100)
    Length= models.DecimalField(max_digits=4,decimal_places=2)
    Width= models.DecimalField(max_digits=4,decimal_places=2)
    Height= models.DecimalField(max_digits=4,decimal_places=2)
    def __str__(self):
        return self.Name
    
    class Meta:
        constraints=[
            models.UniqueConstraint(fields=['Name','Image'], name='unique keyboard')
        ]
        