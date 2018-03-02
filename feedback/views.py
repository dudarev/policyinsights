from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from .models import Feedback
from .forms import FeedbackForm


class FeedbackCreate(CreateView):
    model = Feedback
    form_class = FeedbackForm

    def get_success_url(self):
        return reverse('feedback-thanks')

    def form_valid(self, form):
        feedback = form.save(commit=False)
        feedback.user = self.request.user
        feedback.save()
        return HttpResponseRedirect(self.get_success_url())