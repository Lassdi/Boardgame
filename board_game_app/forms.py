from django import forms
from .models import Boardgame, Review

class BoardgameForm(forms.ModelForm):
    class Meta:
        model = Boardgame
        fields = ['text']
        labels = {'text': ''}

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        labels ={'text': 'Review'}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}