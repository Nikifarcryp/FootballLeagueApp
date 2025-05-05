from django.contrib import admin
from django.urls import path
from .views import index, finder, player, team

urlpatterns = [
    path('', index, name='index'),
    path('find-player/', finder, name='finder'),
    path('player/', player, name='player'),
    path('best_team/', team, name='best_team'),
]
