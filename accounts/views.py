from django.shortcuts import render
from .forms import RegisterForm


def register(request):
    form = RegisterForm(request.POST or None)
    context = {
        "title": "Register",
        "content": "Register Form",
        "form": form,
        "display": "d-none"
    }
    return render(request, 'register.html', context)
