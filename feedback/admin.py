from django.contrib import admin

# Register your models here.

from .models import Feedback, FeedbackEmail


admin.site.register(Feedback)
admin.site.register(FeedbackEmail)
