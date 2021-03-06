from django.http import Http404
from django.shortcuts import render
from django.views import View


class CompareSelectView(View):
    model = None
    template = None
    recent_objects_str = ''

    def get(self, request, **kwargs):
        try:
            object = self.model.objects.get(pk=kwargs['pk'])
        except self.model.DoesNotExist:
            raise Http404("Object does not exist")
        recent_objects_ids = request.session.get(self.recent_objects_str, []),
        recent_objects_ids_without_current = recent_objects_ids[0]
        if object.id in recent_objects_ids_without_current:
            recent_objects_ids_without_current.remove(object.id)
        recent_objects = self.model.objects.filter(pk__in=recent_objects_ids_without_current)
        return render(
            request,
            self.template,
            {
                'object': object,
                'recent_objects': recent_objects,
                'all_objects': self.model.objects.all(),
            }
        )


class CompareView(View):
    model = None
    comparison_model = None
    template = None

    def get(self, request, **kwargs):
        try:
            object1 = self.model.objects.get(pk=kwargs['pk1'])
            object2 = self.model.objects.get(pk=kwargs['pk2'])
            comparison_object, is_created = self.comparison_model.objects.get_or_create(
                object_1=kwargs['pk1'], object_2=kwargs['pk2'])
        except self.model.DoesNotExist:
            raise Http404("Object does not exist")
        return render(request, self.template,
                      {'object1': object1, 'object2': object2, 'comparison_object': comparison_object})
