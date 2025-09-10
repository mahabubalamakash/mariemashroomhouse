from django.db import models
from django.contrib.auth.models import User,Group
import time
from random import Random
# Create your models here.

class profile_model(models.Model):
    times = time.strftime("%I : %M : %S %p")
    dates = time.strftime("%d - %m - %y")

    username = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile_model")
    address = models.CharField(max_length=400,blank=True,null=True)
    phone = models.CharField(max_length=400,blank=True,null=True)
    password1 = models.CharField(max_length=400,blank=True,null=True)
    password2 = models.CharField(max_length=400,blank=True,null=True)
    profile_image = models.ImageField(upload_to='profile',default='defult_profile_image/defult_profile.png')
    is_saller = models.BooleanField(max_length=50,blank=False,null=True)
    welcome_notification = models.CharField(max_length=50,blank=False,null=True,default='Welcome')
    #-----------------Convert Username String----------------------------#
    def __str__(self):
        return str(self.username)


class upload_product(models.Model):
    product_image = models.ImageField(upload_to='product_image',default=True)
    product_name = models.CharField(max_length=5000,blank=True,null=True)
    ammount = models.CharField(max_length=200,blank=True,null=True)
    details = models.CharField(max_length=2000,blank=True,null=True)
    saller = models.ForeignKey(to=profile_model,on_delete=models.CASCADE,related_name='saller')
    def  __str__(self):
        return str(self.saller)


class blog_model(models.Model):
    bloger = models.ForeignKey(to=profile_model,on_delete=models.CASCADE,related_name='bloger')
    video_image = models.FileField(upload_to='blog content',blank=True,null=True)
    #-----------------Convert Username String----------------------------#
    def __str__(self):
        return str(self.bloger)

class home_dalevery_model(models.Model):
    item_name = models.CharField(max_length=200,blank=True,null=True)
    weight = models.CharField(max_length=200,blank=True,null=True)
    customars_name1 = models.ForeignKey(to=profile_model,on_delete=models.CASCADE,related_name='customars_name1')
    customars_address = models.CharField(max_length=400,blank=True,null=True)
    customars_phone = models.CharField(max_length=400,blank=True,null=True)
    home_product_image = models.ImageField(upload_to='home_order_image')
    def __str__(self):
        return str(self.customars_name1)

class kuriar_dalevery_model(models.Model):
    item_name = models.CharField(max_length=200,blank=True,null=True)
    weight = models.CharField(max_length=200,blank=True,null=True)
    customars_name2 = models.ForeignKey(to=profile_model,on_delete=models.CASCADE,related_name='customars_name2')
    customars_phone = models.CharField(max_length=400,blank=True,null=True)
    kuriar_address = models.CharField(max_length=1000,blank=True,null=True)
    kuriar_product_image = models.ImageField(upload_to='kuriar_order_image')
    def __str__(self):
        return str(self.customars_name2)


class send_message(models.Model):
    sender = models.ForeignKey(to=profile_model,on_delete=models.CASCADE,related_name='sender')
    recever = models.ForeignKey(to=profile_model,on_delete=models.CASCADE,related_name='recever')
    text_message = models.CharField(max_length=1000,blank=True,null=True)
    seen = models.BooleanField(max_length=100,blank=False,null=True)
    def __str__(self):
        return str(self.sender)

class upload_videos(models.Model):
    uploder_name = models.ForeignKey(to=profile_model,on_delete=models.CASCADE,related_name='uploder_name')
    upload_video = models.FileField(upload_to='blog content',blank=True,null=True)
    def __str__(self):
        return str(self.uploder_name)