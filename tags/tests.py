# from django.test import TestCase
from unittest import TestCase

from .models import extract_tags
from .templatetags.tags_filters import add_tag_links


class TestTemplateTags(TestCase):
    def test_add_tag_links_no_link(self):
        no_tags_content = "Some content: without tags, does not get\ntags\n"
        self.assertNotIn('href', add_tag_links(no_tags_content))

    def test_single_tag(self):
        tags_content = "Some content: without tags, does not get\ntags\nsome_tag: some content"
        self.assertIn('href', add_tag_links(tags_content))


class TestExtractTags(TestCase):
    def test_extract_tags(self):
        text = "Some content: without tags, does not get\ntags\nsome_tag: some content"
        res = extract_tags(text)
        expected_res = {"some_tag": "some content"}
        self.assertEqual(res, expected_res)
