from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, JsonResponse
from django.views.generic import DetailView, UpdateView, CreateView, ListView
from django.urls import reverse
from django.utils.translation import gettext as _

from policyinsights.views import CompareView, CompareSelectView
from .models import Program
from .forms import ProgramCreateForm, ProgramUpdateForm


N_RESULTS_IN_AUTOCOMPLETE = 10


class ProgramCreate(LoginRequiredMixin, CreateView):

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
        recent_programs = self.request.session.get('recent_programs', [])
        if not self.object.pk in recent_programs:
            recent_programs = [self.object.pk, ] + recent_programs
            recent_programs = recent_programs[:settings.NUMBER_OF_RECENT]
        self.request.session['recent_programs'] = recent_programs
        context = {
            'importance': self.object.importance
        }
        return super().get_context_data(**context)


class ProgramUpdate(LoginRequiredMixin, GetProgramMixin, UpdateView):

    model = Program
    form_class = ProgramUpdateForm

    def get_success_url(self):
        return reverse('program-detail', args=[self.object.location.slug, self.object.slug])


class ProgramCompareSelect(CompareSelectView):
    model = Program
    template = 'programs/compare_select.html',
    recent_objects_str = 'recent_programs'


class ProgramsCompare(CompareView):
    model = Program
    template = 'programs/compare.html'


def autocomplete(request):
    term = request.GET.get('term', '')
    if term:
        qs = Program.objects.filter(slug__icontains=term).all()[:N_RESULTS_IN_AUTOCOMPLETE]
        data = [{'value': str(p), 'id': p.id} for p in qs]
        return JsonResponse(data, safe=False)
    return JsonResponse([], safe=False)

