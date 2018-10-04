from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from efunding.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login, authenticate
    
def home(request):
    return render(request, 'efunding/home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if  form.is_valid():
            form.save()
            return redirect('/profile/')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'efunding/register.html', args)

def view_profile(request):
    args = {'user', request.user}
    return render(request, 'efunding/profile.html')

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'efunding/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/profile')
        else:
            return redirect('/change-password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'efunding/change_password.html', args)