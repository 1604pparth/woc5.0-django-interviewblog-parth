"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from WOC import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout, name='logout'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('home', views.home, name='home'),
    path('gen', views.gen, name='gen'),
    path('myposts', views.myposts, name='myposts'),
    path('profile/<str:pk>', views.oprof, name='oprof'),
    path('editpost/<str:pid>', views.ep, name='ep'),
    path('like_post', views.like_post, name='like_post'),
    path('delete_post', views.delete_post, name='delete_post'),
    path('delete_profile', views.delete_profile, name='delete_profile'),
    path('like_like_post', views.like_like_post, name='like_like_post'),
    path('likedpost', views.likedpost, name='likedpost'),

    path('reset_password', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('accounts/login/', views.alt_way, name="alt_way"),
]

# handler404 = 'WOC.views.error_404_view'
