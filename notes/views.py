from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from .forms import NoteForm


class NoteCreateView(CreateView):
    form_class = NoteForm
    template_name = "notes/create_note.html"

    def form_valid(self, form):
        self.selected_notebook = form.cleaned_data["notebook"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("notebooks:notes_list", args=[str(self.selected_notebook.id)])
