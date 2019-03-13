from django.shortcuts import render


def index(request):
    context = {
        "title": "Welcome",
        "content": "Home Index"
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        "title": "About Us",
        "content": "About Us Page"
    }
    return render(request, 'index.html', context)


def contact(request):
    context = {
        "title": "Contact Us",
        "content": "Contact Us Page"
    }
    return render(request, 'index.html', context)
