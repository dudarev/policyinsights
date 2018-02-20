from django.forms import CharField, ModelForm, Textarea

from locations.models import Location


class LocationForm(ModelForm):
    content = CharField(label='', widget=Textarea)

    class Meta:
        model = Location
        fields = ['content', 'slug', ]
