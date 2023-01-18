from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from WOC.models import Profile, Post


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

                send_mail('Welcome To DA-IICT Interview Blog Community', 'welcome to community',
                          'djangoautomailsystem@gmail.com',
                          [email], fail_silently=False)

                return redirect('settings')
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
    return render(request, 'profile.html', {'user_profile': user_profile})

@login_required(login_url='login')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)
    user_himself = User.objects.get(username=request.user.username)

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

            user_profile.profile_photo = image
            user_profile.first_name = fname
            user_profile.last_name = lname
            user_profile.degree = deg
            user_profile.year = year
            user_profile.program = prog
            user_profile.save()

        if request.FILES.get('profile_photo') != None:
            image = request.FILES.get('profile_photo')
            fname = request.POST['first_name']
            lname = request.POST['last_name']
            deg = request.POST['degree']
            year = request.POST['year']
            prog = request.POST['program']

            user_profile.profile_photo = image
            user_profile.first_name = fname
            user_profile.last_name = lname
            user_profile.degree = deg
            user_profile.year = year
            user_profile.program = prog
            user_profile.save()

        return redirect('profile')

    return render(request, 'settings.html', {'user_profile': user_profile , 'user_himself':user_himself})


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
    if len(posts)!=0:
        return render(request, 'home.html', {'user_profile': user_profile, 'posts': posts})
    else:
        return render(request, 'nopost.html')

def gen(request):
    return render(request, 'general.html')

def myposts(request):
    user_profile = Profile.objects.get(user=request.user)
    posts = Post.objects.filter(creator=user_profile).values()
    if len(posts)!=0:
        return render(request, 'myposts.html', {'user_profile': user_profile, 'posts': posts})
    else:
        return render(request, 'nopostpersonal.html')

