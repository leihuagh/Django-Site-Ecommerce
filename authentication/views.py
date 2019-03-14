from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm


def login_view(request):
    form = LoginForm(request.POST or None)
    context = {
        "title": "Login",
        "content": "Login Form",
        "form": form,
        "display": "d-none"
    }
    if form.is_valid():
        # print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            context["display"] = "d-block"
            form = LoginForm()
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')
