import re

from django import template
from django.urls import reverse


register = template.Library()


RE_FOR_TAGS_TO_COMPARE = r'.*(median_|_capita|_percent|_rate)'
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


@register.inclusion_tag('tags/compared_content.html')
def render_compared_content(page1, page2):
    content_1 = _strip_parameters(page1.content)
    content_2 = _strip_parameters(page2.content)
    return {
        'content_1': content_1,
        'content_2': content_2,
    }


def _get_compared_parameters(parameters_1, parameters_2, style=1):
    compared_parameters = []
    for p in parameters_1:
        if p in parameters_2 and re.match(RE_FOR_TAGS_TO_COMPARE, p):
            value1 = float(NON_DECIMAL.sub('', parameters_1[p]))
            value2 = float(NON_DECIMAL.sub('', parameters_2[p]))
            if value1 > value2:
                if style == 1:
                    compared_parameters.append('{}: <span class="larger">{}</span>'.format(p, parameters_1[p]))
                else:
                    compared_parameters.append('{}: <span class="larger2">{}</span>'.format(p, parameters_1[p]))
                continue
            else:
                if style == 1:
                    compared_parameters.append('{}: <span class="smaller">{}</span>'.format(p, parameters_1[p]))
                else:
                    compared_parameters.append('{}: <span class="smaller2">{}</span>'.format(p, parameters_1[p]))
                continue
        compared_parameters.append('{}: {}'.format(p, parameters_1[p]))
    return compared_parameters


@register.inclusion_tag('tags/compared_parameters.html')
def render_compared_parameters(page1, page2, style=1):
    parameters_1 = _get_parameters(page1.content)
    parameters_2 = _get_parameters(page2.content)
    compared_parameters_1 = _get_compared_parameters(parameters_1, parameters_2, style)
    compared_parameters_2 = _get_compared_parameters(parameters_2, parameters_1, style)
    return {
        'parameters_1': compared_parameters_1,
        'parameters_2': compared_parameters_2,
    }
