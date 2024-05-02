from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField(default=True)
    
    def __str__(self):
        return self.username


class Image(models.Model):
    image_file = models.ImageField(upload_to='image-uploads/', default='', null=True)
    image_name = models.CharField(max_length=100, null=True, default="")
    heading = models.CharField(max_length=100, null=True, default="")
    subheading = models.CharField(max_length=100, null=True, default="")
    banner = models.BooleanField(default=False)
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name



class Blog(models.Model):
    blog_file = models.ImageField(upload_to='blog-uploads/', default='', null=True)
    heading = models.CharField(max_length=100, null=True, default="")
    subheading = models.CharField(max_length=100, null=True, default="")
    body = models.CharField(max_length=500, null=True, default="")
    date_created= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading


class Video(models.Model):
    video_file = models.CharField(max_length=5000, null=True, default="")
    video_name = models.CharField(max_length=100, null=True, default="")
    banner = models.BooleanField(default=False)
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.video_name


class Verifications(models.Model):
    email = models.EmailField(max_length=254)
    token = models.CharField(max_length=50)
    verified = models.BooleanField(default=False)
    

    def __str__(self):
        return self.email


class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, default="")
    email = models.EmailField(max_length=254)
    message = models.CharField(max_length=500, null=True, default="")
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name