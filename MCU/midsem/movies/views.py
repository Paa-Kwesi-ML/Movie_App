from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from .models import *
import datetime
#from .models import Rating

def home(request):
    return render(request, 'home.html')
def main(request):
    return render(request, 'main.html')

def success_page(request):
    return render(request, 'success_page.html')



def logins(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']

        user = auth.authenticate(username=username, password = password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'home.html')
            # return redirect('homepage')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('/')
    return render(request, 'logins.html')


def register(request):
    now = datetime.datetime.now()
    if request.method == 'POST':
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        bday = request.POST['bday']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        gender = request.POST['gender']
        username =firstname +" "+lastname

        if password == cpassword:
            if User.objects.filter(username = username).exists():
                messages.info(request, "Username Taken")
                return redirect('/')
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, password=password)
                user.save()
                profile = UsersDetail.objects.create(Name=username, Gender=gender, birth_date= bday, start_date=now.strftime("%Y-%m-%d"))
                profile.save()
                return redirect('home')
            messages.info(request, "Password mismatch")
            return redirect('logins')

    return render(request, 'register.html')

@login_required(login_url='/')
def logout(request):
    auth.logout(request)
    return redirect('/')

# @login_required(login_url='/')
# def homepage(request):
#     # user = User.objects.get(username=request.user.username)
#     return render(request, 'home.html')

def m1(request):
    return render(request, 'm1.html')
def m2(request):
    return render(request, 'm2.html')
def m3(request):
    return render(request, 'm3.html')
def m4(request):
    return render(request, 'm4.html')
def m5(request):
    return render(request, 'm5.html')
def m6(request):
    return render(request, 'm6.html')
def m7(request):
    return render(request, 'm7.html')
def m8(request):
    return render(request, 'm8.html')
def m9(request):
    return render(request, 'm9.html')
def m10(request):
    return render(request, 'm10.html')
def about(request):
    return render(request, 'about.html')

mmovies = {
    'Spiderman': {
        'title': 'Spiderman',
        'poster_url': '{% static "image/sp man.jpg" %}',
        'release_year': 2018,
        'summary': 'A young farmboy joins a rebellion against an evil empire.'
    },
    'Venom': {
        'title': 'Venom',
        'poster_url': '{% static "images/Venom1.jpg" %}',
        'release_year': 2019,
        'summary': 'A computer hacker discovers a hidden world of virtual reality.'
    },
}
