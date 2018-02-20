from django.views.generic import DetailView, UpdateView, CreateView
from django.urls import reverse

from .models import Program
from .forms import ProgramCreateForm


class ProgramCreate(CreateView):

    model = Program
    success_url = '/'
    form_class = ProgramCreateForm


class ProgramDetail(DetailView):

    model = Program


class ProgramUpdate(UpdateView):

    model = Program
    fields = ['content', 'slug', ]

    def get_success_url(self):
        return reverse('program-detail', args=[self.object.slug])
