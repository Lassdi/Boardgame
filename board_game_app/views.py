from django.shortcuts import render, redirect
from .models import Boardgame
from .forms import Boardgame, BoardgameForm, Review, ReviewForm
from django.contrib.auth.decorators import login_required


def index(request):
    #the home page for app
    return render(request, "board_game_app/index.html")

@login_required
def boardgames(request):
    boardgames = Boardgame.objects.order_by("date_added")
    context = {"boardgames":boardgames}
    return render(request,"board_game_app/boardgames.html", context)

@login_required
def boardgame(request, boardgame_id):
    boardgame = Boardgame.objects.get(id = boardgame_id)
    reviews = boardgame.review_set.order_by("-date_added")
    context = {"boardgame":boardgame, "reviews":reviews}
    return render(request,"board_game_app/boardgame.html",context)


@login_required
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

@login_required
def new_review(request, boardgame_id):
    """Add a new review for a particular board game."""
    boardgame = Boardgame.objects.get(id = boardgame_id)
    if request.method != 'POST':   
        form = ReviewForm()
    else:
        form = ReviewForm(data = request.POST)
        if form.is_valid():
            new_review = form.save(commit = False)
            new_review.boardgame = boardgame
            new_review.save()
            return redirect('board_game_app:boardgame', boardgame_id = boardgame_id)
    context = {'boardgame': boardgame, 'form': form}
    return render(request, 'board_game_app/new_review.html', context)

@login_required
def edit_review(request, review_id):
    """Edit an existing review."""
    review = Review.objects.get(id = review_id)
    boardgame = review.boardgame
    if request.method != 'POST':
        form = ReviewForm(instance = review)
    else:
        form = ReviewForm(instance = review, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_game_app:boardgame', boardgame_id = boardgame.id)
    context = {'review': review, 'boardgame': boardgame, 'form': form}
    return render(request, 'board_game_app/edit_review.html', context)