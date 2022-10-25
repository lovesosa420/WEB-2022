from django.contrib import admin
from bmstu_lab import views
from django.conf.urls.static import static
from django.conf import settings
from rooms import views as stock_views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'buildings', stock_views.BuildingViewSet)
router.register(r'rooms', stock_views.RoomViewSet)

urlpatterns = [
    path('register/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('', views.welcome),
    path('buildings/', views.Building, name='building_url'),
    path('buildings/<str:name_building>', views.Room, name='room_url'),
    path('buildings/<str:name_building>/<str:name_room>', views.Unit, name='unit_url'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


