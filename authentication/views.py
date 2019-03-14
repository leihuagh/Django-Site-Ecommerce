from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    context = {
        "title": "Login",
        "content": "Login Form",
    }
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')
