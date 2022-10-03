from django.shortcuts import render


def welcome(request):
    return render(request, 'welcome.html')


def GetOrders(request):
    return render(request, 'sneakers.html', {'data' : {
        'sneakers': [
            {'title': 'Dark Iris', 'id': 'DarkIris', 'release': '10.09.2019'},
            {'title': 'Katrina', 'id': 'Katrina', 'release': '10.09.2018'},
            {'title': 'Racer Blue', 'id': 'RacerBlue', 'release': '10.09.2017'},
        ]
    }})


def GetOrder(request, id, release):
    return render(request, 'unit.html', {'data' : {
        'id': id,
        'release': release,
    }})
