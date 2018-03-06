from django.http import Http404
from django.views.generic import DetailView, UpdateView, CreateView
from django.urls import reverse
from django.utils.translation import gettext as _

from policyinsights.views import CompareView
from .models import Program
from .forms import ProgramCreateForm, ProgramUpdateForm


class ProgramCreate(CreateView):

    model = Program
    form_class = ProgramCreateForm

    def get_success_url(self):
        return reverse('program-detail', args=[self.object.location.slug, self.object.slug])


class GetProgramMixin:

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug', '')
        location_slug = self.kwargs.get('location_slug', '')
        try:
            object = self.model.objects.filter(slug=slug, location__slug=location_slug).get()
        except self.model.DoesNotExist:
            raise Http404(_("Program does not exist."))
        return object


class ProgramDetail(GetProgramMixin, DetailView):

    model = Program

    def get_context_data(self, **kwargs):
       context = {
           'importance': self.object.importance
       }
       return super().get_context_data(**context)


class ProgramUpdate(GetProgramMixin, UpdateView):

    model = Program
    form_class = ProgramUpdateForm

    def get_success_url(self):
        return reverse('program-detail', args=[self.object.location.slug, self.object.slug])


class ProgramsCompare(CompareView):
    model = Program
    template = 'programs/compare.html'
