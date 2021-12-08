from django import forms
from .models import Boardgame

class BoardgameForm(forms.ModelForm):
    class Meta:
        model = Boardgame
        fields = ['text']
        labels = {'text': ''}