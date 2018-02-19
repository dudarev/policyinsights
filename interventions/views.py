from copy import copy

from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView

from .models import Intervention, InterventionCategory, Location
from .forms import InterventionFilterForm, CaseStudyForm


class LocationsSearchView(ListView):

    model = Location

    def get_queryset(self):
        queryset = Location.objects.all()
        if self.request.GET.get('q'):
            queryset = queryset.filter(name__icontains=self.request.GET.get('q'))
        return queryset


class LocationDetail(DetailView):

    model = Location


class InterventionCategoriesSearchView(ListView):

    model = InterventionCategory

    def get_queryset(self):
        queryset = InterventionCategory.objects.all().filter(location=self.kwargs.get('location_pk'))
        if self.request.GET.get('q'):
            queryset = queryset.filter(name__icontains=self.request.GET.get('q'))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['location'] = Location.objects.get(pk=self.kwargs.get('location_pk'))
        return context


class InterventionsSearchView(ListView):

    model = Intervention

    def get_queryset(self):
        intervention_category_pk = self.kwargs.get('intervention_category_pk')
        queryset = Intervention.objects.filter(category=intervention_category_pk)
        if self.request.GET:
            form = InterventionFilterForm(self.request.GET)
            queryset = queryset.filter(cost__gte=form.data['cost_from'])
            queryset = queryset.filter(cost__lte=form.data['cost_to'])
            queryset = queryset.filter(status__in=form.data.getlist('status'))
            queryset = queryset.filter(type__in=form.data.getlist('type'))
            queryset = queryset.filter(methodology__in=form.data.getlist('methodology'))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        intervention_category = InterventionCategory.objects.get(
            pk=self.kwargs.get('intervention_category_pk'))
        context['intervention_category'] = intervention_category
        context['location'] = intervention_category.location
        # if not GET parameters are specified all checkboxes are selected
        if not self.request.GET:
            base_fields = copy(InterventionFilterForm.base_fields)
            base_fields.pop('cost_from')
            base_fields.pop('cost_to')
            initial = {f: [c[0] for c in base_fields[f].choices] for f in base_fields}
            initial['cost_from'] = 0
            initial['cost_to'] = 1000000000
        else:
            initial = self.request.GET
        context['form'] = InterventionFilterForm(initial)
        return context


class InterventionsDetailView(DetailView):

    model = Intervention


def intervention_csv_view(request, pk):
    response = HttpResponse(content_type='text/csv')
    try:
        intervention = Intervention.objects.get(pk=pk)
        csv_data = intervention.csv_data
    except Intervention.DoesNotExist:
        csv_data = ''
    if not csv_data:
        csv_data = ''
    response.write(csv_data)
    return response


class CaseStudyFormView(FormView):
    template_name = 'case_study_form.html'
    form_class = CaseStudyForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.save()
        return super(CaseStudyFormView, self).form_valid(form)
