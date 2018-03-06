from django import template

register = template.Library()

import re

from django import template
from django.urls import reverse

register = template.Library()

RE_FOR_TAGS_TO_COMPARE = r'.*(median_|_per_capita|_percent)'
NON_DECIMAL = re.compile(r'[^\d.]+')


def _add_tag_links_to_line(line):
    matching_object = re.match(r'(\w+):', line)
    if matching_object:
        tag_slug = matching_object.groups()[0]
        value = line.rsplit(':')[1]
        link = reverse('tag-detail', args=[tag_slug])
        return '<a href="{}">{}</a>: {}'.format(link, tag_slug, value)
    return line


def _has_parameter(line):
    matching_object = re.match(r'(\w+):', line)
    if matching_object:
        return True
    else:
        return False


def _parse_parameter(line):
    matching_object = re.match(r'(\w+):', line)
    if matching_object:
        tag_slug = matching_object.groups()[0]
        value = line.rsplit(':')[1]
        return {tag_slug: value}
    else:
        return {}


def _strip_parameters(content):
    """Strip parameters from content."""
    return "\n".join([line for line in content.splitlines() if not _has_parameter(line)])


def _get_parameters(content):
    """Get parameters from content."""
    res = {}
    for line in content.splitlines():
        parameter_dict = _parse_parameter(line)
        res.update(parameter_dict)
    return res


@register.inclusion_tag('tags/compared_page.html')
def render_compared(page1, page2):
    content_without_parameters = _strip_parameters(page1.content)
    page1_parameters = _get_parameters(page1.content)
    page2_parameters = _get_parameters(page2.content)
    compared_parameters = []
    for p in page1_parameters:
        if p in page2_parameters and re.match(RE_FOR_TAGS_TO_COMPARE, p):
            value1 = float(NON_DECIMAL.sub('', page1_parameters[p]))
            value2 = float(NON_DECIMAL.sub('', page2_parameters[p]))
            if value1 > value2:
                compared_parameters.append('{}: <span class="larger">{}</span>'.format(p, page1_parameters[p]))
                continue
            else:
                compared_parameters.append('{}: <span class="smaller">{}</span>'.format(p, page1_parameters[p]))
                continue
        compared_parameters.append('{}: {}'.format(p, page1_parameters[p]))
    return {
        'content': content_without_parameters,
        'parameters': compared_parameters,
    }
