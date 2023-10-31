from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_view, name='articles'),
    path('create/', views.create_article_view, name='create'),
]
