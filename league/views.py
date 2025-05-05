from django.shortcuts import render
from .models import Standing, Team, Player
# Create your views here.

def index(request):
    standings = Standing.objects.all().order_by('-points')
    return render(request, 'standings.html', context={'standings': standings})

def finder(request):
    if request.method == 'GET':
        return render(request, 'team_finder.html')
    return None

def player(request):
    if request.method == 'POST':
        team = request.POST.get('team')
        team = ' '.join(map(lambda x: x.capitalize(), team.split(' ')))
        player = Player.get_scorer_against_team(team)
        return render(request, 'best_player.html', context={'team_name': team, 'player': player})
    return None

def team(request):
    if request.method == 'GET':
        return render(request, 'best_team.html', context={'best_team': Team.get_the_best_team()})
    return None
