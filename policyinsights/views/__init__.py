from django.http import Http404
from django.shortcuts import render
from django.views import View


class CompareView(View):
    model = None
    template = None

    def get(self, request, **kwargs):
        try:
            object1 = self.model.objects.get(pk=kwargs['pk1'])
            object2 = self.model.objects.get(pk=kwargs['pk2'])
        except self.model.DoesNotExist:
            raise Http404("Object does not exist")
        return render(request, self.template, {'object1': object1, 'object2': object2})
