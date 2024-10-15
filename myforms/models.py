from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()

class Post(models.Model):
    title=models.CharField(max_length=100)
    summary=models.TextField()
    content=models.TextField()