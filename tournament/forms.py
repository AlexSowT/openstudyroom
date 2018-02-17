from django import forms
from django.contrib.auth.models import Group
from django.forms import ModelForm
from .models import Tournament, TournamentGroup
import pytz

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = [
            'name',
            'begin_time',
            'end_time',
            'tag',
            'main_time',
            'byo_time',
            'is_open',
            'is_public',
            'description',
        ]
        widgets = {
            'name': forms.TextInput(),
            'begin_time': forms.SelectDateWidget(),
            'end_time': forms.SelectDateWidget(),
        }

class TournamentGroupForm(ModelForm):
    class Meta:
        model = TournamentGroup
        fields = ['name']