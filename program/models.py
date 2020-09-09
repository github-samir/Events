from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Member(models.Model):
  user = models.OneToOneField(User,on_delete=models.SET_NULL, null=True)
  name = models.CharField(max_length=200)
  phonenumber = models.CharField(max_length=50,blank=True)
  email = models.EmailField(blank=True)
  address = models.CharField(max_length=50)
  
  def __str__(self):
    return self.name

class Venue(models.Model):
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	phonenumber = models.CharField(max_length=50,blank=True)
	email = models.EmailField(blank=True)
	
	def __str__(self):
	  return self.name

class Event(models.Model):
  name=models.CharField(max_length=100)
  event_date = models.DateField()
  venue = models.ForeignKey(Venue,on_delete=models.SET_NULL,null=True,blank=False)
  manager=models.ForeignKey(Member,related_name='manager',on_delete=models.SET_NULL,null=True)
  description = models.CharField(max_length=200,blank=True)
  attendes = models.ManyToManyField(Member)
  
  def __str__(self):
    return self.name