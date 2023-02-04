from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def reg(request):
    if request.user.is_authenticated:
        return redirect('prof')
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                form.save()
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('prof')

    return render(request, 'users/register.html')


def log(request):
    if request.user.is_authenticated:
        return redirect('prof')
    else:
        if request.method == 'POST':
            username = request.post.get('username')
            password = request.post.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('prof')

    return render(request, 'users/login.html')


@login_required(login_url='log')
def prof(request):
    return render(request, 'users/profile.html')


def lout(request):
    logout(request)
    return redirect(request, 'log')
