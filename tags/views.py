from django.views.generic import DetailView, UpdateView, CreateView, ListView
from django.urls import reverse

from .models import Tag
from .forms import TagForm


class TagCreateUpdateMixin():

    model = Tag
    form_class = TagForm

    def get_success_url(self):
        return reverse('tag-detail', args=[self.object.slug])


class TagCreate(TagCreateUpdateMixin, CreateView):

    pass


class TagDetail(DetailView):

    model = Tag

    def get_context_data(self, **kwargs):
        context = super(TagDetail, self).get_context_data()
        # TODO: get programs for tag or do not implement?
        # programs = self.object.program_set.all()
        # context.update({'programs': programs})
        return context


class TagUpdate(TagCreateUpdateMixin, UpdateView):

    pass


class TagList(ListView):

    model = Tag
