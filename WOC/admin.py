from django.contrib import admin

# Register your models here.
from .models import Profile

admin.site.register(Profile)

from .models import Post

admin.site.register(Post)

from .models import AddProf

admin.site.register(AddProf)

from .models import LikePost

admin.site.register(LikePost)