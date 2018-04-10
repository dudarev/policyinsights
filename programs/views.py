from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views.generic import DetailView, UpdateView, CreateView, RedirectView

from policyinsights.views import CompareView, CompareSelectView
from .forms import ProgramCreateForm, ProgramUpdateForm
from .models import Program, UserProgram

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
        try:
            if self.request.user.is_authenticated:
                user_program = UserProgram.objects.get(program=self.object, user=self.request.user)
            else:
                user_program = None
        except UserProgram.DoesNotExist:
            user_program = None
        context = {
            'importance': self.object.importance,
            'user_program': user_program
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
        qs = Program.objects.filter(
            Q(slug__icontains=term) | Q(search_keywords__icontains=term)
        ).all()[:N_RESULTS_IN_AUTOCOMPLETE]
        data = [{'value': str(p), 'id': p.id} for p in qs]
        return JsonResponse(data, safe=False)
    return JsonResponse([], safe=False)


class ProgramFollow(LoginRequiredMixin, RedirectView):

    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        program = get_object_or_404(Program, pk=kwargs['pk'])
        if 'unfollow' in self.request.path:
            try:
                user_program = UserProgram.objects.get(program=program, user=self.request.user)
                user_program.delete()
            except UserProgram.DoesNotExist:
                pass
            messages.add_message(self.request, messages.SUCCESS, 'You unfollowed the program.')
        else:
            followed_programs_count = UserProgram.objects.filter(user=self.request.user).count()
            if followed_programs_count >= settings.MAX_FOLLOW_COUNT:
                messages.add_message(
                    self.request,
                    messages.ERROR,
                    'You follow {} programs. To follow more programs, <a href="{}">request</a> a premium account.'.format(
                        followed_programs_count,
                        reverse('feedback')
                    )
                )
            else:
                messages.add_message(self.request, messages.SUCCESS, 'You followed the program.')
                UserProgram.objects.get_or_create(program=program, user=self.request.user)
        return reverse('program-detail', args=[program.location.slug, program.slug])
