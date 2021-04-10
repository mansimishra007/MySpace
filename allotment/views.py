from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, LoginForm
from django.http import HttpResponse, Http404
from allotment.models import Student, Room, Hostel
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Welcome page
def welcome(request):
	return render(request, 'allotment/welcome.html')

# Student Home Page  
def home (request):
    return render(request, 'allotment/home.html')

# Show Hostel Info
def show_hostel_info(request):
	return render(request, 'allotment/hostel_info.html')

# Student Register Page
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            Student.objects.create(user=new_user)
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password1'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('login/edit/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = UserRegisterForm()
        args = {'form': form}
        return render(request, 'allotment/register.html', args)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password'])
            if user is not None:
                if user.is_warden:
                    return HttpResponse('Invalid Login')
                if user.is_active:
                    login(request, user)
                    student = request.user.student
                    return render(request, 'allotmrnt/profile.html', {'student': student})
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
        return render(request, 'allotment/login.html', {'form': form})



# Student Profile   
#@login_required
#def profile(request):
#    return render(request, 'users/profile.html')