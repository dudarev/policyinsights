from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import DetailView, UpdateView, CreateView, ListView
from django.urls import reverse
from django.http import Http404

from .models import Tag
from .forms import TagForm


class TagCreateUpdateMixin():
    model = Tag
    form_class = TagForm

    def get_success_url(self):
        return reverse('tag-detail', args=[self.object.slug])


class TagCreate(LoginRequiredMixin, TagCreateUpdateMixin, CreateView):
    def get_initial(self):
        return {'slug': self.request.GET.get('slug', '')}


class TagDetail(DetailView):
    model = Tag

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            return redirect("{}?slug={}".format(reverse('tag-create'), self.kwargs.get('slug', '')))
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class TagUpdate(LoginRequiredMixin, TagCreateUpdateMixin, UpdateView):
    pass
