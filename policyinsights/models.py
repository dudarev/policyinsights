import copy

from django.db import models
from django.http import Http404


class ComparisonManager(models.Manager):
    """
    This manager makes `get` and `get_or_create` return the same comparison object
    independent on order of compared objects.
    The objects are re-ordered so that the first one is with smaller pk.

    `compared_model` must be specified in the managers that inherit from this one.
    """
    compared_model = None

    def _get_normalized_kwargs(self, **kwargs):
        new_kwargs = copy.copy(kwargs)
        object_1 = new_kwargs.get('object_1', None)
        object_2 = new_kwargs.get('object_2', None)
        if not isinstance(object_1, self.compared_model):
            try:
                object_1 = self.compared_model.objects.get(pk=object_1)
            except self.model.DoesNotExist:
                raise Http404("Object does not exist")
        if not isinstance(object_2, self.compared_model):
            try:
                object_2 = self.compared_model.objects.get(pk=object_2)
            except self.model.DoesNotExist:
                raise Http404("Object does not exist")
        if object_1.pk > object_2.pk:
            object_1, object_2 = object_2, object_1
        new_kwargs['object_1'] = object_1
        new_kwargs['object_2'] = object_2
        return new_kwargs

    def get(self, *args, **kwargs):
        new_kwargs = self._get_normalized_kwargs(**kwargs)
        return super().get(*args, **new_kwargs)

    def get_or_create(self, defaults=None, **kwargs):
        new_kwargs = self._get_normalized_kwargs(**kwargs)
        return super().get_or_create(defaults, **new_kwargs)
