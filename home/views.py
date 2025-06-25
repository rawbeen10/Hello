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
    return HttpResponse("This is about page")

def services(request):
    return HttpResponse("This is services page")

def contact(request):
    return HttpResponse("This is contact page")