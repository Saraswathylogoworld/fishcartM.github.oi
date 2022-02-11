from django.db import models
from fishapp.models import pfish
from django.db.models.deletion import CASCADE

# Create your models here.
class freg(models.Model):
    uname = models.CharField(max_length=200,null=True,blank=False) 
    password =models.CharField(max_length=200,null=True,blank=False)
    repassword =models.CharField(max_length=200,null=True,blank=False)  
    location = models.CharField(max_length=200,null=True,blank=False) 
    number = models.IntegerField(null=True,blank=False) 
    email = models.CharField(max_length=200,null=True,blank=False)
    adrs = models.CharField(max_length=200,null=True,blank=False)
    img = models.ImageField(upload_to='image',null=True,blank=False)    

    
class Fwcart(models.Model):
    productid = models.ForeignKey(pfish,on_delete=CASCADE,null=True,blank=True)
    userid = models.ForeignKey(freg,on_delete=CASCADE,null=True,blank=False)
    total = models.IntegerField(null=True,blank=False)
    quantity = models.IntegerField(null=True,blank=False)
    status = models.IntegerField(null=True,blank=False)

class Fview_contact(models.Model):
    message = models.TextField(max_length=200,null=True,blank=False) 
    name = models.CharField(max_length=200,null=True,blank=False) 
    email = models.CharField(max_length=200,null=True,blank=False) 
    subject = models.TextField(max_length=200,null=True,blank=False) 

class FCheckout(models.Model):
    cartid = models.ForeignKey(Fwcart,on_delete=CASCADE,null=True,blank=False)
    fname = models.CharField(max_length=200,null=True,blank=False)
    email = models.EmailField(null=True,blank=False)
    mobile = models.IntegerField(blank=False,null=True)
    address = models.TextField(max_length=200,null=True,blank=False)       