from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def users_view(request):
    # return HttpResponse("Liste des utilisateurs")
    return render(request,'users/list.html')

def create_users_view(request):
    return HttpResponse("Creer un utilisateur")