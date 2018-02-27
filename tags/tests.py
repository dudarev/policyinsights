# from django.test import TestCase
from unittest import TestCase

from .templatetags.tags_filters import add_tag_links


class TestTemplateTags(TestCase):
    def test_add_tag_links_no_link(self):
        no_tags_content = "Some content: without tags, does not get\ntags\n"
        self.assertNotIn('href', add_tag_links(no_tags_content))

    def test_single_tag(self):
        no_tags_content = "Some content: without tags, does not get\ntags\nsome_tag: some content"
        self.assertIn('href', add_tag_links(no_tags_content))
