from django.forms import CharField, ModelForm, Textarea

from .models import Feedback


class FeedbackForm(ModelForm):
    content = CharField(label='', widget=Textarea)

    class Meta:
        model = Feedback
        fields = ['content', ]
