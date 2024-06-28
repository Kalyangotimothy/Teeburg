from django.db import models
import datetime

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='events/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class NurseryUpdate(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='nursery_updates/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class PrimaryUpdate(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='primary_updates/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class StaffUpdate(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='staff_updates/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.caption or self.image.name