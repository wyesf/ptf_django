from django.shortcuts import render

# Create your views here.
def landing(request) :
    return render(
        request,
        'single_pages/landing.html'
    )

def about_me(request) :
    return render(
        request,
        'single_pages/about_me.html'
    )

def contact(request) :
    return render(
        request,
        'single_pages/contact.html'
    )

def projects(request) :
    return render(
        request,
        'single_pages/projects.html',
    )
    
def toypjt(request) :
    return render(
        request,
        'single_pages/toy_main.html',
    )
    
