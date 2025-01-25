from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .forms import UserForm
from .models import CustomUser
from statemanager.urls import user_action_tree_view
from statemanager.models import State



def UserRegistration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.current_state = State.objects.get(name="initial_interview")
            user.save()

            messages.success(request, f'Account created for {form.cleaned_data["username"]}')
            return redirect('login')
        else:
            messages.error(request, 'Please fill all the fields.')
    else:
        form = UserForm()

    return render(request, 'register.html', {'form': form})


def UserLogin(request):
   if request.method=='POST':
       username = request.POST['username']
       password = request.POST['password']
       user = authenticate(request, username=username, password=password)

       if user is not None:
           login(request, user)
           messages.success(request, f'You are now logged in')
           return redirect('user-action-tree', user_id=user.id)
       else:
           messages.error(request, 'Invalid username or password.')
           return redirect('login')

   else:
    return render(request, 'login.html')



















