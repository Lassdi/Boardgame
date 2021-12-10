#Defines url patterns for Board_game_app

from django.urls import path
from . import views
app_name = 'board_game_app'

urlpatterns = [
    path('', views.index, name='index'), #Home page
    path('boardgame/', views.new_boardgame, name = 'new_boardgame'), #Adding a new board game
    path('boardgames/', views.boardgames, name= 'boardgames'), #List of all board games
    path('boardgames/<int:boardgame_id>/', views.boardgame, name= 'boardgame'), #Individual boardgame
    path("new_review/<int:boardgame_id>/", views.new_review, name="new_review"), #Writing a new review
    path("edit_review/<int:review_id>/", views.edit_review, name="edit_review"), #Edoting a review
]