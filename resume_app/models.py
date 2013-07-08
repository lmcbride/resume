from django.db import models
from datetime import datetime
class Person(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city  = models.CharField(max_length=50)
    state = models.CharField(max_length=15)
    zip = models.IntegerField(max_length=5, default=True)
    telephone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

class Skills(models.Model):
    category = models.ForeignKey('Category', null=True, default=None)
    name = models.CharField(max_length=50,default='')
    
    def __unicode__( self ):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, default='')
    
    def __unicode__( self ):
        return self.name
    
class Projects(models.Model):
    description = models.CharField(max_length=250)
  
class Experience(models.Model):
    company = models.CharField(max_length=50)
    begin_date = models.DateField(auto_now=False, auto_now_add=False)    
    end_date = models.DateField(default = None,null=True, blank=True, auto_now_add=False)   
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    description_2 = models.CharField(max_length=250, default=True)
    description_3 = models.CharField(max_length=250, default=True)
    
    