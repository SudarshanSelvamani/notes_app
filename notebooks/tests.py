from django.test import TestCase
from django.urls import reverse, resolve


from . import views
from notes.models import Note, Notebook


class Mixin:
    def create_notebook(self, name="English"):
        return Notebook.objects.create(name=name)

    def create_note(self, title="Chapter1", body="jigsaw", notebook=None):
        if notebook == None:
            notebook = self.create_notebook()
        return Note.objects.create(title=title, body=body, notebook=notebook)


class TestNoteListView(TestCase, Mixin):
    def setUp(self):
        self.note = self.create_note()

    def test_page_serve_successful(self):
        url = reverse("notebooks:notes_list", args=[self.note.pk])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolve_note_list_object(self):
        view = resolve(f"/notebooks/{self.note.pk}/notes")
        self.assertEquals(view.func.view_class, views.NoteListView)


class TestNoteBookCreateView(TestCase, Mixin):
    def test_page_serve_successful(self):
        url = reverse("notebooks:create_notebook")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolve_notebook_create_object(self):
        view = resolve("/notebooks/create")
        self.assertEquals(view.func, views.notebook_create_popup)

    def test_presence_of_csrf(self):
        url = reverse("notebooks:create_notebook")
        response = self.client.get(url)
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_note_save(self):

        self.client.post(
            "/notebooks/create",
            {
                "name": "Test Notebook",
            },
        )

        self.assertEqual(Notebook.objects.last().name, "Test Notebook")


class TestNoteBookUpdateView(TestCase, create_mixin.Mixin):
    def setUp(self):
        self.notebook = self.create_notebook()

    def test_page_serve_successful(self):
        url = reverse("notebooks:update_notebook", args=[self.notebook.pk])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolve_notebook_update_object(self):
        view = resolve(f"/notebooks/{self.notebook.pk}/update")
        self.assertEquals(view.func.view_class, views.NotebookUpdateView)

    def test_presence_of_csrf(self):
        url = reverse("notebooks:update_notebook", args=[self.notebook.pk])
        response = self.client.get(url)
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_note_save(self):

        self.client.post(
            f"/notebooks/{self.notebook.pk}/update",
            {
                "name": "Test Notebook",
            },
        )

        self.assertEqual(Notebook.objects.last().name, "Test Notebook")
