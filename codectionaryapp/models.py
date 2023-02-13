from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from PIL import Image
from django.urls import reverse


# Create your models here.

class Creator(models.Model):
    email  = models.EmailField(unique=True);
    name  = models.CharField(max_length=100);
    channel_name  = models.CharField(max_length=100,unique=True);
    street_address  = models.CharField(max_length=100);
    country  = models.CharField(max_length=100);
    city  = models.CharField(max_length=100);
    zip_code  = models.IntegerField(default=00);
    date_of_birth  = models.DateField(auto_now=False, auto_now_add=False);
    channel_catagory  = models.CharField(max_length=100);
    channel_banner  = models.ImageField(upload_to='img/');
    channel_logo  = models.ImageField(upload_to='img/');
    about  = models.CharField(max_length=500);
    github  = models.CharField(max_length=500,default='')
    user = models.OneToOneField(User,on_delete= models.CASCADE, default='')
    date_joined = models.DateField(auto_now=True);
    def __str__(self):
        return self.channel_name
    
    def get_absolute_url(self):
        return reverse('profile',args=[str(self.channel_name)])


class Content(models.Model):
    id = models.IntegerField( unique=True, auto_created=True, editable=False, primary_key=True,)
    title =  models.CharField(max_length=55)
    desciption = models.CharField(max_length=200,  default='')
    video = models.FileField(upload_to='videos/', null=False)
    content = RichTextField()
    views = models.IntegerField(default=0,editable=False)
    rating  = models.FloatField(default=0,editable=False)
    likes = models.IntegerField(default=0,editable=False)
    creator = models.ForeignKey(Creator,on_delete= models.CASCADE,null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/')
    date_uploaded = models.DateField(auto_now=True);
    tags = models.CharField(max_length=100,default='')
    github = models.CharField(max_length=500,default='')
    linkedin = models.CharField(max_length=500,default='')
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/watch?content='+ str(self.id)


class Like(models.Model):
    id = models.IntegerField( unique=True, auto_created=True, editable=False, primary_key=True,)
    content = models.ForeignKey(Content,on_delete= models.CASCADE,null=False)
    liker = models.ForeignKey(User,on_delete= models.CASCADE,null=False,default=1)
    time = models.DateField(auto_now=True);

class View(models.Model):
    id = models.IntegerField( unique=True, auto_created=True, editable=False, primary_key=True,)
    content = models.ForeignKey(Content,on_delete= models.CASCADE,null=False)
    time = models.DateField(auto_now=True);

class Follower(models.Model):
    id = models.IntegerField( unique=True, auto_created=True, editable=False, primary_key=True,)
    followed_by = models.ForeignKey(User,on_delete= models.CASCADE,null=False,default=1,related_name='followed_by')
    follow_to = models.ForeignKey(Creator,on_delete= models.CASCADE,null=False,default=1,related_name="follow_to")
    time = models.DateField(auto_now=True);

class Comments(models.Model):
    id = models.IntegerField( unique=True, auto_created=True, editable=False, primary_key=True,)
    commentor = models.ForeignKey(User,on_delete= models.CASCADE,null=False,default=1,related_name='commentor')
    content = models.ForeignKey(Content,on_delete= models.CASCADE,null=False) 
    text = models.CharField(max_length=500)
    time = models.DateField(auto_now=True);
    def __str__(self):
        return self.text

class Saves(models.Model):
    id = models.IntegerField( unique=True, auto_created=True, editable=False, primary_key=True,)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False,default=1)
    content = models.ForeignKey(Content,on_delete= models.CASCADE,null=False)  
    time = models.DateField(auto_now=True);
