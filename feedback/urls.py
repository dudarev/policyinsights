from django.urls import path
from django.views.generic import TemplateView

from feedback import views


urlpatterns = [
    path('feedback/', views.FeedbackCreate.as_view(), name='feedback'),
    path('feedback/thanks/', TemplateView.as_view(template_name='feedback/thanks.html'), name='feedback-thanks'),
]

