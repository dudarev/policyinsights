from annoying.fields import AutoOneToOneField
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = AutoOneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=5, null=True, blank=False, default=None)

    def __str__(self):
        return self.user.username