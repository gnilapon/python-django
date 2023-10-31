from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('about/', views.about_view, name='about'),
    #path('article/', views.article_view, name='article'),
    path('articles/', include('articles.urls'), name='articles'),
    path('users/', include('users.urls')),
]
