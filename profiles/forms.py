from django import forms
from registration.forms import RegistrationForm

from django.utils.translation import ugettext_lazy as _


class CustomRegistrationForm(RegistrationForm):
    required_css_class = 'required'
    zip_code = forms.CharField(min_length=5, max_length=5, required=True, label=_("ZIP code"))

    def save(self, commit=True):
        user = super().save(commit=commit)
        user.profile.zip_code = self.cleaned_data['zip_code']
        user.profile.save()
        return user
