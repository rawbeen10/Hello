from django.shortcuts import render
from django.shortcuts import HttpResponse, render

# Create your views here.
def index(request):
    context = {
        'variable1': "this is variable context",
        'variable2': "this is second variable."
    }
    # return HttpResponse("This is home page")
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')