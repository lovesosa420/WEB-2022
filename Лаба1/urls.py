from django.contrib import admin
from django.urls import path
from bmstu_lab import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome),
    path('buildings/', views.Building, name='building_url'),
    path('buildings/<str:name_building>', views.Room, name='room_url'),
    path('buildings/<str:name_building>/<str:name_room>', views.Unit, name='unit_url'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


