from django.shortcuts import render
from bmstu_lab.models import Building_c
from bmstu_lab.models import Room_c


def welcome(request):
    return render(request, 'welcome.html')


def Building(request):
    return render(request, 'building.html', {'data': {
        'buildings': Building_c.objects.all()
    }})


def Room(request, name_building):
    return render(request, 'rooms.html', {'data': {
        'rooms': Room_c.objects.filter(building=name_building),
        'name_building': name_building,
    }})


def Unit(request, name_building, name_room):
    return render(request, 'unit.html', {'data': {
        'unit': Room_c.objects.get(name_room=name_room),
    }})
