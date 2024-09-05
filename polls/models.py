from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    descripsen=models.TextField()
    image = models.ImageField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=50)
    valus = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Reyting(models.Model):
    class Soni(models.TextChoices):
        star_5 = "5",
        star_4 = "4",
        star_3 = "3",
        star_2 = "2",
        star_1 = "1",
        star_0 = "0",
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(max_length=2, choices=Soni.choices, default=Soni.star_0)



class Comment(models.Model):
    class Likes(models.TextChoices):
        like = '👍🏻'
        notlike = '👎🏻'

    text = models.TextField()
    like = models.CharField(max_length=2, choices=Likes.choices, default=Likes.like)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Banner(models.Model):
    image = models.ImageField()
    url = models.URLField()

class Settings(models.Model):
    telegram_urls = models.URLField()
    facebook_urls = models.URLField()
    twitter_urls = models.URLField()
    instagram_urls = models.URLField()
