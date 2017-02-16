from django import forms
from models import Sms
from twittersearch.models import Topics, Datefilters
from django.contrib.auth.models import User






class SendsmsForm(forms.Form):
    subscribed_topic = forms.ModelChoiceField(queryset=User.objects.none(),  label='Please select your name')
    message = forms.CharField(widget=forms.Textarea, max_length=255, label='Please enter your message')
    # choices = forms.ModelChoiceField(queryset=Searches.objects.none(),
    #                                  label='select twittersearch')


    def __init__(self, request, *args, **kwargs):
        super(SendsmsForm, self).__init__(*args, **kwargs)
        if request.user:
            queryset = User.objects.filter(username=request.user)
        else:
            queryset = User.objects.all()

        self.fields['subscribed_topic'].queryset = queryset

    # class Meta:
    #     model = Sms
    #     fields = [
    #         'subscribed_topic'
    #     ]

class SmssearchForm(forms.Form):
    searchword = forms.CharField(max_length=255, label='Enter your twittersearch word', required=True, widget=forms.TextInput())
    select_option = forms.ModelChoiceField(queryset=Datefilters.objects.all(), widget=forms.Select(), label='Filter With', required=True)




