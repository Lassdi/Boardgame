from django.shortcuts import render, redirect
from .models import Boardgame
from .forms import Boardgame, BoardgameForm


def index(request):
    #the home page for app
    return render(request, 'Board_game_app/index.html')

def new_Boardgame(request):
    if request.method != 'POST':
        form = BoardgameForm
    else:
        form = BoardgameForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Board_game_app:topics')
        context = {'form':form}
        return render(request, 'Board_game_app/new_Boardgame.html', context)