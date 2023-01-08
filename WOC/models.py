from django.db import models
from django.contrib.auth import get_user_model

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
