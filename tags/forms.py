from django.forms import CharField, ModelForm, Textarea

from .models import Tag


class TagForm(ModelForm):
    content = CharField(label='', widget=Textarea)

    class Meta:
        model = Tag
        fields = ['content', 'slug', ]
