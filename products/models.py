from django.db import models
from datetime import datetime

class Product (models.Model):
    CHOICES = [
        ('cell phone','mobile'),
        ('computer','laptop')
    ]
    name = models.CharField(max_length=50,verbose_name='title')
    content = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    image = models.ImageField(upload_to='photos/%y/%m/%d',verbose_name='photo' ,default='photos/1/product.png')
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=15,choices=CHOICES)

    def __str__ (self) :
        return self.name
    
    class Meta : 
        ordering = ['name']


class TestDateAndTime (models.Model):
    date = models.DateField()
    time = models.DateField(null=True)
    created = models.DateTimeField(default=datetime.now)
