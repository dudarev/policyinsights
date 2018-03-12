import re

from django import template
from django.urls import reverse

register = template.Library()


def _add_tag_links_to_line(line):
    matching_object = re.match(r'(\w+):', line)
    if matching_object:
        tag_slug = matching_object.groups()[0]
        value = line.split(':', 1)[1]
        link = reverse('tag-detail', args=[tag_slug])
        return '<a href="{}">{}</a>: {}'.format(link, tag_slug, value)
    return line


def add_tag_links(value):
    """Add links to tag pages"""
    return "\n".join([_add_tag_links_to_line(line) for line in value.splitlines()])


register.filter('add_tag_links', add_tag_links)
