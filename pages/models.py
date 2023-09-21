from django.db import models


# Create your models here.

## practice database relations

# 1- One to one relation 
class Female (models.Model):
    name_female = models.CharField(max_length=50,null=True)
    def __str__(self) :
        return self.name_female

class Male (models.Model):
    name_male = models.CharField(max_length=50,null=True)
    girl = models.OneToOneField(Female,on_delete=models.CASCADE)
    def __str__(self) :
        return self.name_male
    

# one to many relation 
class Items (models.Model):
    title = models.CharField(max_length=50,null=True)
    def __str__(self) :
        return self.title
    
class User (models.Model):
    name = models.CharField(max_length=50,null=True)
    products = models.ForeignKey(Items,on_delete=models.CASCADE)
    def __str__(self) :
        return self.name
    
# many to many relation 
class Video (models.Model):
    title = models.CharField(max_length=50,null=True)
    def __str__(self) :
        return self.title
    
class UserVideo (models.Model):
    name = models.CharField(max_length=50,null=True)
    watch = models.ManyToManyField(Video,null=True)
    def __str__(self) :
        return self.name
    
#### test form 
class Login (models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)    