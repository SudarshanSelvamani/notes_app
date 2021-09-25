from django.test import TestCase
from django.urls import reverse, resolve

import test_mixin.create_mixin as create_mixin
from notes.models import Notebook, Note
from . import views


class TestNotebookListView(TestCase, create_mixin.Mixin):
    def test_page_serve_successful(self):
        url = reverse("notebooks:notebook_list")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolve_notebook_list_object(self):
        view = resolve("/notebooks/")
        self.assertEquals(view.func.view_class, views.NotebookListView)
