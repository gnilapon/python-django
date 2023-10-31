from django.shortcuts import render
from django.http import HttpResponse
from blog.db_articles import articles

# Create your views here.

def article_view(request):
    # return HttpResponse("Liste des utilisateurs")
    return render(request,'articles/list.html',context={'articles': articles})

def create_article_view(request):
    return HttpResponse("Creer un article")