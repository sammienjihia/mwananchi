from django import forms
from models import Topics, Subscribers





class SubscriptionForm(forms.ModelForm):
    mobile_number = forms.CharField(max_length=255, label='Phone Number')
    subscribed_topic = forms.ModelChoiceField(queryset=Topics.objects.all(), widget=forms.Select(), label='Topic')

    class Meta:
        model = Subscribers
        fields = [
            'mobile_number',
            'subscribed_topic'
        ]

    def clean_mobile_number(self):
        mobile_number = self.cleaned_data.get('mobile_number')
        if Subscribers.objects.filter(mobile_number=self.cleaned_data.get('mobile_number')).count():
            raise forms.ValidationError("This mobile number is already subscribed")
        return mobile_number

    def clean_subscribed_topic(self):
        subscribed_topic = self.cleaned_data.get('subscribed_topic')
        return subscribed_topic


