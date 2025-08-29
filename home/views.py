from django.shortcuts import render
from django.shortcuts import HttpResponse, render
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    menu_items = [
    {
        "name": "Momo",
        "description": "Nepali Momo",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Momo_nepal.jpg/500px-Momo_nepal.jpg",
        "prep_time": "20 mins"
    },
    {
        "name": "French Fries",
        "description": "Classic French fries with a crispy exterior",
        "image_url": "https://thecozycook.com/wp-content/uploads/2020/02/Copycat-McDonalds-French-Fries-.jpg",
        "prep_time": "15 mins"
    },
    
    {
        "name": "Spring Rolls",
        "description": "Crispy spring rolls with vegetables",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Spring_Rolls.jpg/500px-Spring_Rolls.jpg",
        "prep_time": "25 mins"
    }
]

    # return HttpResponse("This is home page")
    messages.success(request, "This is a success message.")
    return render(request, 'index.html', {'menu_items': menu_items})

def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        date = datetime.today()
        contact = Contact(name=name, email=email, message=message, date=date)
        contact.save()
        messages.success(request, "Your feedback has been submitted successfully!")

    return render(request, 'contact.html')