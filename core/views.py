from itertools import count
from django.shortcuts import render;
from random import randint

def home(request):
    games = []
    repeats=[]
    if request.POST:
        num = int(request.POST['numero'] )
        for i in range(num):
            game = []
            count=0
            while count < 6:
                x = randint(1, 60)
                if x not in game: 
                    game.append(x)
                    count+=1
            game.sort()
            games.append(game)
        for h in range(1, 60):
            count = 0
            for g in games:
                if h in g:
                    count += 1
            repeats.append(count)

    cont = {'dados': games, 'rep': repeats}

    return render(request, 'index.html', cont)
