from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

#publish manager returns posts with PUBLISHED status
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status= Post.Status.PUBLISHED)
#posts model
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
    #makes slug out of title of the post
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    objects = models.Manager()
    published = PublishedManager()
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)    
    name = models.CharField(max_length=80)
    email =models.EmailField(max_length=254)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
   #meta class for ordering comments
    class Meta:
        ordering = ['created_on']
        managed = True
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
    
    def __str__(self):
        return f"comment {self.body} on {self.post} by {self.name}" 

     
