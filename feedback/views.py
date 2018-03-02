from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Feedback
from .forms import FeedbackForm
from .email import send_email_about_feedback


class FeedbackCreate(CreateView):
    model = Feedback
    form_class = FeedbackForm
    success_url = reverse_lazy('feedback-thanks')

    def form_valid(self, form):
        feedback = form.save(commit=False)
        feedback.user = self.request.user
        feedback.save()
        self.object = feedback
        send_email_about_feedback(self.request, feedback)
        return HttpResponseRedirect(self.get_success_url())