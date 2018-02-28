import re

from django.db import models


def extract_tags(text):
    """
    Returns a dict of tag-values parsed from `text`: `{tag: value}`.
    It can be useful to populate JSONField for tags.
    """
    res = {}
    for line in text.splitlines():
        matching_object = re.match(r'(\w+):', line)
        if matching_object:
            tag_slug = matching_object.groups()[0]
            value = line.rsplit(':')[1].strip()
            try:
                value = int(value)
            except:
                pass
            res[tag_slug] = value
    return res


class Tag(models.Model):
    slug = models.SlugField(max_length=200, null=False, unique=True)
    content = models.TextField(max_length=2000, blank=True, default='')

    def __str__(self):
        return self.slug
