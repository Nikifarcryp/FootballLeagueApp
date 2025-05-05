from django.contrib import admin
from .models import Goal, Standing, Match, Player, Team
from .forms import MatchAdminForm

# Register your models here.

admin.site.register(Goal)
admin.site.register(Standing)
admin.site.register(Player)
admin.site.register(Team)

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    form = MatchAdminForm
    list_display = ('home_team_id', 'away_team_id', 'date', 'result')
    list_filter = ('date', 'result')
