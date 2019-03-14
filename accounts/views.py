from django.shortcuts import render


def register(request):
    context = {
        "title": "Register",
        "content": "Register Form"
    }
    return render(request, 'register.html', context)
