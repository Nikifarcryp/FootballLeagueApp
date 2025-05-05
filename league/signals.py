from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Team, Standing, Match, Goal


@receiver(post_save, sender=Team)
def create_or_update_standings(sender, instance, created, **kwargs):
    if created:
        standing, _ = Standing.objects.get_or_create(team_id=instance)
        standing.save()

@receiver(post_save, sender=Match)
def update_standings(sender, instance, **kwargs):
    home_team_standing = Standing.objects.get(team_id=instance.home_team_id)
    away_team_standing = Standing.objects.get(team_id=instance.away_team_id)

    if instance.result == Match.ResultOptions.HOME_WIN:
        home_team_standing.wins += 1
        home_team_standing.points += 3
        away_team_standing.losses += 1
    elif instance.result == Match.ResultOptions.AWAY_WIN:
        away_team_standing.wins += 1
        away_team_standing.points += 3
        home_team_standing.losses += 1
    elif instance.result == Match.ResultOptions.DRAW:
        home_team_standing.draws += 1
        away_team_standing.draws += 1
        home_team_standing.points += 1
        away_team_standing.points += 1

    home_team_standing.matches_played += 1
    away_team_standing.matches_played += 1

    home_team_standing.save()
    away_team_standing.save()