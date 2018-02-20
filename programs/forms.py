from django.core.exceptions import ValidationError
from django.forms import Field, CharField, ModelForm, Textarea
from django.utils.translation import gettext as _

from locations.models import Location

from .models import Program


class LocationSlugField(Field):
    def to_python(self, value):
        try:
            location = Location.objects.get(slug=value)
            return location
        except Location.DoesNotExist:
            raise ValidationError(
                _('Invalid location slug: %(value)s'),
                params={'value': value},
            )


class DisabledLocationSlugField(Field):
    def prepare_value(self, value):
        if value:
            location = Location.objects.get(pk=value)
            return location.slug
        return value


class ProgramCreateForm(ModelForm):
    location = LocationSlugField(label='Location slug')
    content = CharField(label='', widget=Textarea)

    class Meta:
        model = Program
        fields = ['content', 'slug', 'location', ]


class ProgramUpdateForm(ProgramCreateForm):
    location = DisabledLocationSlugField(label='Location slug', disabled=True)

    def clean_location(self):
        # do not update location
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
          return instance.location
        else:
          return self.cleaned_data['location']
