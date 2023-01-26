import datetime
import email

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from WOC.models import Profile, Post, AddProf, LikePost


# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pass1']
        password2 = request.POST['pass2']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        deg = request.POST['degree']
        program = request.POST['program']
        year = request.POST['year']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                # log user in and redirect to settings page

                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                # create profile object for new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id, first_name=fname,
                                                     last_name=lname, degree=deg, program=program, year=year)
                new_profile.save()
                add_prof = AddProf.objects.create(main_user=new_profile, ctc=-1, insta_prof='none',
                                                  linkedin_prof='none', position='DuMmY', placed_at='DuMmY')
                add_prof.save()

                send_mail('Welcome To DA-IICT Interview Blog Community', 'welcome to community',
                          'djangoautomailsystem@gmail.com',
                          [email], fail_silently=False)

                return redirect('home')
        else:
            messages.info(request, 'Password not matching')
            return redirect('signup')


    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Credentials invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')


@login_required(login_url='login')
def profile(request):
    user_profile = Profile.objects.get(user=request.user)
    user_add_profile = AddProf.objects.get(main_user=user_profile)
    return render(request, 'profile.html', {'user_profile': user_profile, 'user_add_profile': user_add_profile})


@login_required(login_url='login')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)
    user_himself = User.objects.get(username=request.user.username)
    user_add_profile = AddProf.objects.get(main_user=user_profile)
    # method 2
    # user_object = User.objects.get(username=request.user.username)
    # user_profile = Profile.objects.get(user=user_object)

    if request.method == 'POST':

        if request.FILES.get('profile_photo') == None:
            image = user_profile.profile_photo
            fname = request.POST['first_name']
            lname = request.POST['last_name']
            deg = request.POST['degree']
            year = request.POST['year']
            prog = request.POST['program']
            pat = request.POST['placed_at']
            pos = request.POST['position']
            ctc = request.POST['ctc']
            lprof = request.POST['linkedin_prof']
            iprof = request.POST['insta_prof']

            if ctc is '':
                ctc = -1
            if pat is '':
                pat = 'DuMmY'
            if pos is '':
                pos = 'DuMmy'
            if lprof is '':
                lprof = 'none'
            if iprof is '':
                iprof = 'none'

            user_profile.profile_photo = image
            user_profile.first_name = fname
            user_profile.last_name = lname
            user_profile.degree = deg
            user_profile.year = year
            user_profile.program = prog
            user_profile.save()

            user_add_profile.ctc = ctc
            user_add_profile.insta_prof = iprof
            user_add_profile.linkedin_prof = lprof
            user_add_profile.placed_at = pat
            user_add_profile.position = pos
            user_add_profile.save()

        if request.FILES.get('profile_photo') != None:
            image = request.FILES.get('profile_photo')
            fname = request.POST['first_name']
            lname = request.POST['last_name']
            deg = request.POST['degree']
            year = request.POST['year']
            prog = request.POST['program']
            pat = request.POST['placed_at']
            pos = request.POST['position']
            ctc = request.POST['ctc']
            lprof = request.POST['linkedin_prof']
            iprof = request.POST['insta_prof']

            if ctc is '':
                ctc = -1
            if pat is '':
                pat = 'DuMmY'
            if pos is '':
                pos = 'DuMmy'
            if lprof is '':
                lprof = 'none'
            if iprof is '':
                iprof = 'none'

            user_profile.profile_photo = image
            user_profile.first_name = fname
            user_profile.last_name = lname
            user_profile.degree = deg
            user_profile.year = year
            user_profile.program = prog
            user_profile.save()

            user_add_profile.ctc = ctc
            user_add_profile.insta_prof = iprof
            user_add_profile.linkedin_prof = lprof
            user_add_profile.placed_at = pat
            user_add_profile.position = pos
            user_add_profile.save()

        return redirect('profile')

    return render(request, 'settings.html',
                  {'user_profile': user_profile, 'user_himself': user_himself, 'user_add_profile': user_add_profile})


@login_required(login_url='login')
def upload(request):
    user_profile = Profile.objects.get(user=request.user)
    user_model = User.objects.get(username=request.user.username)

    if request.method == 'POST':
        user = user_profile.user.username
        cname = request.POST['company_name']
        title = request.POST['title']
        jprofile = request.POST['job_profile']
        otype = request.POST['offer_type']
        year = request.POST['year']
        mblog = request.POST['main_blog']

        new_post = Post.objects.create(user=user, company_name=cname, title=title, job_profile=jprofile,
                                       offer_type=otype,
                                       year=year, main_blog=mblog, creator=user_profile)
        new_post.save()
        return redirect('home')

    else:
        return render(request, 'upload.html')


@login_required(login_url='login')
def home(request):
    user_profile = Profile.objects.get(user=request.user)
    posts = Post.objects.all()
    liked_posts = LikePost.objects.filter(username=request.user).values()
    if len(posts) != 0:
        return render(request, 'home.html', {'user_profile': user_profile, 'posts': posts, 'liked_posts': liked_posts})
    else:
        return render(request, 'nopost.html')


def like_post(request):
    username = request.user.username
    user_profile = Profile.objects.get(user=request.user)
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter is None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.likes = post.likes + 1
        post.liked_by.add(user_profile)
        post.save()
        return redirect('home')
    else:
        like_filter.delete()
        post.likes = post.likes - 1
        post.liked_by.remove(user_profile)
        post.save()
        return redirect('home')


def delete_post(request):
    post_id = request.GET.get('post_id')
    post = Post.objects.get(id=post_id)
    post.delete()
    delete_likes = LikePost.objects.filter(post_id=post_id)
    delete_likes.delete()
    return redirect('myposts')


def delete_profile(request):
    curr_user = User.objects.get(username=request.user.username)
    send_mail('Profile deletion successful', 'We are sorry to lose a very valuable memberof community.',
              'djangoautomailsystem@gmail.com',
              [curr_user.email], fail_silently=False)
    auth.logout(request)
    curr_user.delete()
    return redirect('login')

@login_required(login_url='login')
def alt_way(request):
    return redirect('home')


def error_404_view(request, exception):
    return render(request, '404.html')
def like_like_post(request):
    username = request.user.username
    user_profile = Profile.objects.get(user=request.user)
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter is None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.likes = post.likes + 1
        post.liked_by.add(user_profile)
        post.save()
        return redirect('likedpost')
    else:
        like_filter.delete()
        post.likes = post.likes - 1
        post.liked_by.remove(user_profile)
        post.save()
        return redirect('likedpost')


def gen(request):
    posts = Post.objects.all()
    user_profile = Profile.objects.get(user=request.user)
    liked_posts = LikePost.objects.filter(username=request.user).values()
    return render(request, 'general.html', {'user_profile': user_profile, 'posts': posts, 'liked_posts': liked_posts})


@login_required(login_url='login')
def myposts(request):
    user_profile = Profile.objects.get(user=request.user)
    posts = Post.objects.filter(creator=user_profile).values()
    number_of_post = len(posts)
    if len(posts) != 0:
        return render(request, 'myposts.html',
                      {'user_profile': user_profile, 'posts': posts, 'number_of_post': number_of_post})
    else:
        return render(request, 'nopostpersonal.html')


@login_required(login_url='login')
def oprof(request, pk):
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    user_post = Post.objects.filter(creator=user_profile)
    number_of_post = len(user_post)
    user_add_profile = AddProf.objects.get(main_user=user_profile)

    curr_user = Profile.objects.get(user=request.user)
    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_post': user_post,
        'number_of_post': number_of_post,
        'user_add_profile': user_add_profile,
    }

    if curr_user.user == user_object:
        return render(request, 'profile.html', {'user_add_profile': user_add_profile, 'user_profile': user_profile})
    else:
        return render(request, 'profile_others.html', context)


@login_required(login_url='login')
def ep(request, pid):
    post = Post.objects.get(id=pid)

    if request.method == 'POST':
        cname = request.POST['company_name']
        title = request.POST['title']
        jprofile = request.POST['job_profile']
        otype = request.POST['offer_type']
        year = request.POST['year']
        mblog = request.POST['main_blog']

        post.company_name = cname
        post.title = title
        post.job_profile = jprofile
        post.offer_type = otype
        post.year = year
        post.main_blog = mblog
        post.posted_at = datetime.datetime.now()
        post.save()
        return redirect('myposts')

    return render(request, 'edit_posts.html', {'post': post})


@login_required(login_url='login')
def likedpost(request):
    user_profile = Profile.objects.get(user=request.user)
    posts = Post.objects.all()
    liked_posts = LikePost.objects.filter(username=request.user).values()
    num = len(liked_posts)
    return render(request, 'likedposts.html',
                  {'user_profile': user_profile, 'posts': posts, 'liked_posts': liked_posts, 'num': num})

# def error(request, exception):
#     return render(request, 'error.html', status=404)
