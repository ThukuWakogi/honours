from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    profile_pic = models.ImageField(upload_to='profile-images', default='images/default.jpg')
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Project(models.Model):
    title = models.CharField(max_length=255)
    landing_page_image = models.ImageField(upload_to='profile-images', default='images/default.jpg')
    description = models.TextField()
    link = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)


class ProjectRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rater')
    project = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_rated')
    design = models.IntegerField()
    usability = models.IntegerField()
    content = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
