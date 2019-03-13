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
    return render(request, 'about.html', context)


def contact(request):
    context = {
        "title": "Contact Us",
        "content": "Contact Form"
    }
    if (request.method == 'POST'):
        print(request.POST)
        print(request.POST.get('fullname'))
        print(request.POST.get('email'))
        print(request.POST.get('content'))
    return render(request, 'contact.html', context)
