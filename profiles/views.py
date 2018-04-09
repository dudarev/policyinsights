from django.shortcuts import render
from django.views.generic import DetailView

from profiles.models import Profile
from programs.models import UserProgram


class ProfileDetail(DetailView):
    model = Profile

    def get_object(self, queryset=None):
        return Profile.objects.get_or_create(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(ProfileDetail, self).get_context_data()
        user_programs = UserProgram.objects.filter(user=self.request.user).all()
        context.update({'user_programs': user_programs})
        return context
