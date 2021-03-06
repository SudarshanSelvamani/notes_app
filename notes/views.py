from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import NoteForm
from .models import Note


@method_decorator(login_required, name="dispatch")
class NoteCreateView(CreateView):
    form_class = NoteForm
    template_name = "notes/create_note.html"

    def form_valid(self, form):
        self.selected_notebook = form.cleaned_data["notebook"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("notebooks:notes_list", args=[str(self.selected_notebook.id)])


@method_decorator(login_required, name="dispatch")
class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    pk_url_kwarg = "note_pk"
    template_name = "notes/create_note.html"

    def get_success_url(self):
        return reverse("notebooks:notes_list", args=[self.kwargs.get("pk")])


@method_decorator(login_required, name="dispatch")
class NoteDeleteView(DeleteView):
    model = Note
    pk_url_kwarg = "note_pk"
    template_name = "notes/delete.html"

    def get_success_url(self):
        messages.success(self.request, "Note was deleted successfully.")
        return reverse("notebooks:notes_list", args=[self.kwargs.get("pk")])
