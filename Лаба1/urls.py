from django.contrib import admin
from django.urls import path
from bmstu_lab import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome),
    path('sneakers/', views.Sneakers, name='catalog_url'),
    path('sneakers/<id>/<photo>',  views.Model,  name='sneaker_url'),
]