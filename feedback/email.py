from django.core.mail import EmailMessage
from django.template import Template, Context, loader
from django.urls import  reverse

from .models import FeedbackEmail


def send_email_about_feedback(request, feedback):
    recepients = [e.email for e in FeedbackEmail.objects.all()]
    if recepients:
        template = loader.get_template('feedback/email_to_admins.txt')
        context = {
            'user': feedback.user.username,
            'content': feedback.content,
            'admin_link': request.build_absolute_uri(reverse('admin:feedback_feedback_changelist'))
        }
        template.render(context, request)
        email_content = template.render(context)
        email = EmailMessage(
            'New feedback from {}'.format(feedback.user.username),
            email_content,
            cc=recepients
        )
        email.send()
