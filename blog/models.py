from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Post (models.Model):

    class Status (models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB' , 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    created = models.DateTimeField(default= datetime.now)
    publish = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length= 2, choices= Status.choices, default= Status.DRAFT)


    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = name = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)    
    name = models.CharField(max_length=80)
    email =models.EmailField(max_length=254)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['created_on']
        db_table = ''
        managed = True
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
    
    def __str__(self):
        return f"comment {self.body} on {self.post} by {self.name}" 

     
