from django.db import models
from django.db.models import Count

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)

    @staticmethod
    def get_the_best_team():
        top_team = Team.objects.select_related('standing').order_by('-standing__points').first()
        if top_team:
            return top_team.name, top_team.standing.points if top_team else None
        return None

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)

    @staticmethod
    def get_scorer_against_team(team):
        top_scorer = (
            Goal.objects.filter(opponent_team_id__name=team, is_own_goal=False)
            .values('player_id__name')
            .annotate(goals_against=Count('id'))
            .order_by('-goals_against')
            [:1]
        )
        return top_scorer[0] if top_scorer else None

    def __str__(self):
        return self.name

class Match(models.Model):
    class ResultOptions(models.IntegerChoices):
        HOME_WIN = 1, 'Home Win'
        AWAY_WIN = 2, 'Away Win'
        DRAW = 3, 'Draw'

    date = models.DateField()
    home_team_id = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE, blank=False, null=False)
    away_team_id = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE, blank=False, null=False)
    result = models.IntegerField(choices=ResultOptions.choices, null=True, blank=True)

    def __str__(self):
        return f"{self.home_team_id} vs {self.away_team_id} on {self.date}"


class Goal(models.Model):
    match_id = models.ForeignKey(Match, on_delete=models.CASCADE)
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
    team_id = models.ForeignKey(Team, related_name='scored_goals', on_delete=models.CASCADE)  # забившая команда
    opponent_team_id = models.ForeignKey(Team, related_name='conceded_goals', on_delete=models.CASCADE)
    is_own_goal = models.BooleanField(default=False)

    def __str__(self):
        return f"Goal by {self.player_id} in {self.match_id}"


class Standing(models.Model):
    team_id = models.OneToOneField(Team, on_delete=models.CASCADE, primary_key=True)
    points = models.IntegerField(default=0)
    matches_played = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)

    def __str__(self):
        return (f"{self.team_id.name} - {self.points} pts - {self.matches_played} matches played - "
                f"{self.wins} wins - {self.draws} draws - {self.losses} losses")
