from django.forms import Form, MultipleChoiceField, CheckboxSelectMultiple, DecimalField
from .models import Intervention


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
    cost_from = DecimalField(required=False)
    cost_to = DecimalField(required=False)
