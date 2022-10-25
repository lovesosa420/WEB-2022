from rest_framework import viewsets
from rooms.serializers import BuildingSerializer, RoomSerializer
from rooms.models import Building, Room


class BuildingViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Building.objects.all().order_by('name_building')
    serializer_class = BuildingSerializer  # Сериализатор для модели


class RoomViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Room.objects.all().order_by('building')
    serializer_class = RoomSerializer  # Сериализатор для модели