from django.test import TestCase

from .models import Note, Notebook


class Mixin:
    def create_notebook(self, name="English"):
        return Notebook.objects.create(name=name)

    def create_note(self, title="Chapter1", body="jigsaw", notebook=None):
        if notebook == None:
            notebook = self.create_notebook()
        return Note.objects.create(title=title, body=body, notebook=notebook)
