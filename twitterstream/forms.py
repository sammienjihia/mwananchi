
from django import forms

from search.models import Topics, Datefilters
from django.contrib.auth.models import User









class StreamForm(forms.Form):
    searchword = forms.CharField(max_length=255, label='Enter your search word')
    filename = forms.CharField(max_length=255, label='Enter a file name')
    timedelta = forms.IntegerField( label='Enter the duration for the bot to run: This is in minutes')


class DownloadForm(forms.Form):
    filename = forms.CharField(max_length=255, label='Enter a file name')
