from rooms.models import Building, Room
from rest_framework import serializers


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Building
        # Поля, которые мы сериализуем
        fields = ["name_building"]


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Room
        # Поля, которые мы сериализуем
        fields = ["building", "name_room", "kind", "size", "price", "is_free"]