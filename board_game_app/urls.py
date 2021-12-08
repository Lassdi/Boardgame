#Defines url patterns for Board_game_app

from django.urls import path
from . import views
app_name = 'Board_game_app'

urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    path('new_boardgame/', views.new_boardgame, name = 'new_boardgame'),
]