from django.shortcuts import render, redirect
from .models import Boardgame
from .forms import Boardgame, BoardgameForm


def index(request):
    #the home page for app
    return render(request, "board_game_app/index.html")

def boardgames(request):
    boardgames = Boardgame.objects.order_by("date_added")
    context = {"boardgames":boardgames}
    return render(request,"board_game_app/boardgames.html", context)

def boardgame(request, boardgame_id):
    boardgame = Boardgame.objects.get(id = boardgame_id)
    reviews = boardgame.review_set.order_by("-date_added")
    context = {"boardgame":boardgame, "reviews":reviews}
    return render(request,"board_game_app/boardgame.html",context)



def new_boardgame(request):
    if request.method != "POST":
        form = BoardgameForm()
    else:
        form = BoardgameForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("board_game_app:boardgames")
        context = {"form":form}
        return render(request, "board_game_app/new_boardgame.html", context)