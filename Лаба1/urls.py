from django.contrib import admin
from django.urls import path
from bmstu_lab import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome),
    path('sneakers/', views.GetOrders, name='catalog_url'),
    path('sneakers/<id>/<release>',  views.GetOrder, name='sneaker_url'),
]