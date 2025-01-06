from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth.hashers import make_password

from .models import CustomUser
from .forms import UserForm, SignInForm


def UserRegistration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            messages.success(request, f'Account created for {form.cleaned_data["username"]}')
            return redirect('login')
        else:
            messages.error(request, 'Please fill all the fields.')
    else:
        form = UserForm()

    return render(request, 'register.html', {'form': form})


def UserLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            messages.success(request, f'welcome {user.username}')
        else:
            messages.error(request, 'Invalid Credentials')
    else:
        form = SignInForm()
    return render(request, 'login.html')











