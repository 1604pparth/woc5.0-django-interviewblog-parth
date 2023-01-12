from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from WOC.models import Profile


# Create your views here.
@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html')

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
                messages.info(request,'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #log user in and redirect to settings page

                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                #create profile object for new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id, first_name=fname,
                                                     last_name=lname, degree=deg, program=program, year=year)
                new_profile.save()

                send_mail('Welcome To DA-IICT Interview Blog Community', 'welcome to community', 'djangoautomailsystem@gmail.com',
                          [email], fail_silently=False)

                return redirect('settings')
        else:
            messages.info(request,'Password not matching')
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
            return redirect('profile')
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
def settings(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':

        if request.FILES.get('profile_photo') == None:
            image = user_profile.profile_photo
            fname = request.POST['first_name']

            user_profile.profile_photo = image
            user_profile.first_name = fname
            user_profile.save()

        if request.FILES.get('profile_photo') != None:
            image = request.FILES.get('profile_photo')
            fname = request.POST['first_name']

            user_profile.profile_photo = image
            user_profile.first_name = fname
            user_profile.save()

        return  redirect('settings')

    return render(request, 'settings.html', {'user_profile':user_profile})

@login_required(login_url='login')
def upload(request):
    return render(request, 'upload.html')

