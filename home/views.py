from datetime import datetime
from home.models import Contact
from django.shortcuts import render, HttpResponse

# Create your views here


def index(request):
    # return HttpResponse("This is our homepage.")
    # if anyone comes to the homepage..render the request from the templates that is written in base directory.
    context = {
        'variable': 'Developer Dept',
    }
    return render(request, 'index.html', context)


def about(request):
    # return HttpResponse("This is about our homepage.")
    return render(request, 'about.html')


def river(request):
    # return HttpResponse("Strawberry Shortcakes river fudge !!")
    return render(request, 'river.html')


def service(request):
    # return HttpResponse("This is about service page.")
    return render(request, 'service.html')


def contact(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc, date=datetime.today())
        contact.save()

    return render(request, 'contact.html')
