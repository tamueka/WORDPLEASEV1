from django.contrib import messages
from django.contrib.auth import authenticate, login as login_user_in_django, logout as close_user_sesion
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from users.forms import RegisterForm


def login(request):

    if request.method == 'POST':
        username = request.POST.get('form_username')
        password = request.POST.get('form_password')
        user = authenticate(request, username=username, password=password)
        if user is None:  # si no existe el usuario con ese username/password
            messages.error(request, 'Wrong username or password')
        else:
            # si el usuario existe, tenemos que hacer login del usuario en la sesión
            login_user_in_django(request, user)
            welcome_url = request.GET.get('next', 'home')
        return redirect(welcome_url)

    return render(request, 'users/login.html')


def logout(request):
    close_user_sesion(request)
    messages.success(request, 'You have been logged out succesfully')
    return redirect('home')


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = User()
            new_user.first_name = form.cleaned_data.get('first_name')
            new_user.last_name = form.cleaned_data.get('last_name')
            new_user.username = form.cleaned_data.get('username')
            new_user.email = form.cleaned_data.get('email')
            new_user.set_password(form.cleaned_data.get('password'))
            new_user.save()
            messages.success(request, 'User registered successfully!')
            form = RegisterForm()

    else:
        form = RegisterForm()

    return render(request, 'users/signup.html', {'form': form})

