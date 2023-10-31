from django.shortcuts import render

def home_view(request):
    # return  HttpResponse("Hello word!")
    return render(request, 'home.html')

def contact_view(request):
    # return  HttpResponse("Contact Us")
    return render(request,'contact.html')

def about_view(request):
    # return  HttpResponse("About Us")
    return render(request,'about.html')