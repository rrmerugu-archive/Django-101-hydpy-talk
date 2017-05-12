# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import reverse
# Create your tests here.


class StaticPagesTest(TestCase):
    def test_homepage(self):
        url = reverse('home_page')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)