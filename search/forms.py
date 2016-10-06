from django import forms
from models import Topics, KeyWords


class CascadeForm(forms.Form):
    topic = forms.ModelChoiceField(Topics.objects.all())
    keyword = forms.ModelChoiceField(KeyWords.objects.none())


    def __init__(self, *args, **kwargs):
        forms.Form.__init__(self, *args, **kwargs)
        topics = Topics.objects.all()

        if len(topics) == 1:
            self.fields['topic'].initial= topics[0].pk

            topic_ids = self.fields['topic'].initial or self.initial.get('topic') or self._raw_value('topic')

            if topic_ids:
                keywords = KeyWords.objects.filter(topic=topic_ids)
                self.fields['keywords'].queryset = keywords

                if len(keywords)==1:
                    self.fields['keywords'].initial = keywords[0].pk