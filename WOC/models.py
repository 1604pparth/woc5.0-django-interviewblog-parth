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
    program = models.CharField(max_length=32)
    year = models.IntegerField()

    def __str__(self):
        return self.user.username

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

    def __str__(self):
        return self.user
