from django.shortcuts import render


def welcome(request):
    return render(request, 'welcome.html')


def Sneakers(request):
    return render(request, 'sneakers.html', {'data': {
        'sneakers': [
            {'title': 'Dark Iris', 'id': 'DarkIris', 'photo': 'DarkIris.jpg'},
            {'title': 'Katrina', 'id': 'Katrina', 'photo': 'Katrina.jpg'},
            {'title': 'Racer Blue', 'id': 'RacerBlue', 'photo': 'RacerBlue.jpg'},
        ]
    }})


def Model(request, id, photo):
    photo = 'images/' + photo
    return render(request, 'unit.html', {'data' : {
        'id': id,
        'photo': photo
    }})