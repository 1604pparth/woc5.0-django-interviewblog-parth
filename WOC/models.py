from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    profile_photo = models.ImageField(upload_to='profile_photo', default='default_photo.jpg')
    degree = models.CharField(max_length=32)
    program = models.CharField(max_length=60)
    year = models.IntegerField()

    def __str__(self):
        return self.user.username


class AddProf(models.Model):
    main_user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    ctc = models.IntegerField(default=-1)
    placed_at = models.CharField(max_length=60, default="DuMmY", blank=True)
    position = models.CharField(max_length=60, default="DuMmY", blank=True)
    linkedin_prof = models.TextField(default="none")
    insta_prof = models.TextField(default="none")

    def __str__(self):
        return self.main_user.user.username

class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Post(models.Model):
    user = models.CharField(max_length=30)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    company_name = models.CharField(max_length=255)
    title = models.TextField()
    job_profile = models.CharField(max_length=30)
    offer_type = models.CharField(max_length=30)
    year = models.IntegerField()
    posted_at = models.DateTimeField(default=datetime.now)
    main_blog = models.TextField()
    likes = models.IntegerField(default=0)
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name='+')
    liked_by = models.ManyToManyField(Profile, default=None, blank=True)
    def __str__(self):
        return self.user

