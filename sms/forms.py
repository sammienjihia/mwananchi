from django import forms
from models import Sms
from search.models import Topics





class SendsmsForm(forms.ModelForm):
    #subscribed_topics = forms.ModelChoiceField(queryset=Topics.objects.all(), widget=forms.Select(), label='Topic')


    class Meta:
        model = Sms
        fields = [
            'subscribed_topic'
        ]




