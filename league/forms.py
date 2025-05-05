from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Match

class MatchAdminForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = '__all__'

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date > timezone.now().date():
            raise ValidationError("The date cannot be in the future.")
        return date

    def clean(self):
        cleaned_data = super().clean()
        home_team_id = cleaned_data.get('home_team_id')
        away_team_id = cleaned_data.get('away_team_id')

        print(f"Home Team ID: {home_team_id}, Away Team ID: {away_team_id}")

        if home_team_id and away_team_id and home_team_id == away_team_id:
            raise ValidationError("A team cannot play against itself.")

