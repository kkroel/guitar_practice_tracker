from django import forms
from .models import Song, StudentSong


class NewSongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'composer', 'level', 'description', 'level', 'style', 'genre']


class StudentSongForm(forms.ModelForm):
    class Meta:
        model = StudentSong
        fields = ['tempo', 'tempo_goal', 'purpose', 'status']
