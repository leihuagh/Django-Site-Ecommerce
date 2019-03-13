from django.shortcuts import render
from .forms import ContactForm


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
    form = ContactForm(request.POST or None)
    context = {
        "title": "Contact Us",
        "content": "Contact Form",
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        print(form.cleaned_data.get('fullname'))
        print(form.cleaned_data.get('email'))
        print(form.cleaned_data.get('content'))
        form = ContactForm()
    return render(request, 'contact.html', context)
