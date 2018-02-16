from django.forms import Form, MultipleChoiceField, CheckboxSelectMultiple, DecimalField, ModelForm
from .models import Intervention, CaseStudy


class InterventionFilterForm(Form):
    status = MultipleChoiceField(
        widget=CheckboxSelectMultiple(),
        choices=Intervention.STATUS_CHOICES,
        required=False)
    type = MultipleChoiceField(
        widget=CheckboxSelectMultiple,
        choices=Intervention.TYPE_CHOICES,
        required=False)
    methodology = MultipleChoiceField(
        widget=CheckboxSelectMultiple,
        choices=Intervention.METHODOLOGY_CHOICES,
        required=False)
    cost_from = DecimalField(required=False, initial=0)
    cost_to = DecimalField(required=False, initial=1000000000)


class CaseStudyForm(ModelForm):
    class Meta:
        model = CaseStudy
        fields = ['user_name', 'email', 'program_name', 'more_information']
