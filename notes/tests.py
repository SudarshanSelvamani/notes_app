from django.test import TestCase
from django.urls import resolve, reverse

from .models import Note, Notebook
from . import views


class Mixin:
    def create_notebook(self, name="English"):
        return Notebook.objects.create(name=name)

    def create_note(self, title="Chapter1", body="jigsaw", notebook=None):
        if notebook == None:
            notebook = self.create_notebook()
        return Note.objects.create(title=title, body=body, notebook=notebook)


class TestNoteCreateView(TestCase, Mixin):
    def test_page_serve_successful(self):
        url = reverse("notes:create")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolve_note_create_object(self):
        view = resolve("/notes/create")
        self.assertEquals(view.func.view_class, views.NoteCreateView)

    def test_presence_of_csrf(self):
        url = reverse("notes:create")
        response = self.client.get(url)
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_note_save(self):
        notebook = self.create_notebook()

        self.client.post(
            "/notes/create",
            {
                "title": "Test Note",
                "body": "Test success",
                "notebook": notebook.id,
                "tag": "test",
            },
        )

        self.assertEqual(Note.objects.last().title, "Test Note")


class TestNoteUpdateView(TestCase, create_mixin.Mixin):
    def setUp(self):
        self.notebook = self.create_notebook()
        self.note = self.create_note(notebook=self.notebook)

    def test_page_serve_successful(self):
        url = reverse("notes:update", args=[self.notebook.pk, self.note.pk])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolve_note_update_object(self):
        view = resolve(f"/notes/{self.notebook.pk}/update/{self.note.pk}")
        self.assertEquals(view.func.view_class, views.NoteUpdateView)

    def test_presence_of_csrf(self):
        url = reverse("notes:update", args=[self.notebook.pk, self.note.pk])
        response = self.client.get(url)
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_note_save(self):

        self.client.post(
            f"/notes/{self.notebook.pk}/update/{self.note.pk}",
            {
                "title": "Test Note",
                "body": "Test success",
                "notebook": self.notebook.id,
                "tag": "test",
            },
        )

        self.assertEqual(Note.objects.last().title, "Test Note")
