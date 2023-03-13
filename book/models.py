from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
class Category(models.Model):
    poster = models.ImageField(upload_to='images/',blank=True,verbose_name="Kategoriya posteri")
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
class Contributor(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Muallif")
    audio = models.FileField(upload_to='audios/')
    bookid = models.IntegerField()
class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,verbose_name="Kategoriya")
    author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Muallif")
    title = models.CharField(max_length=500,verbose_name="Sarlavha")
    bio = RichTextField(verbose_name="Kitobdan parcha")
    image = models.ImageField(upload_to='images/', blank=True,verbose_name="Kitob suratini yuklash"),
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Video(models.Model):
    video_title = models.CharField(max_length=500)
    video_link = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.video_title

class Model1(models.Model):
    id = models.BigAutoField(primary_key=True)
