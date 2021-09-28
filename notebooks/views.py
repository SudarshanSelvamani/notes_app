from django.views.generic import ListView, UpdateView
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from notes.models import Notebook, Note
from .forms import NotebookForm


@method_decorator(login_required, name="dispatch")
class NoteListView(ListView):
    model = Note
    paginate_by = 6
    context_object_name = "notes"
    template_name = "notes/note_list.html"

    def get_queryset(self):
        notebook = get_object_or_404(Notebook, pk=self.kwargs.get("pk"))
        if self.request.GET.get("tags"):
            query_tags = self.request.GET.get("tags").split(",")
            return Note.objects.filter(tag__name__in=query_tags, notebook=notebook)
        return Note.objects.filter(notebook=notebook)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["notebooks"] = Notebook.objects.annotate(Count("note"))
        return context


@login_required
def notebook_create_popup(request):
    form = NotebookForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        return HttpResponse(
            '<script>opener.closePopup(window, "%s", "%s", "#id_notebook");</script>'
            % (instance.pk, instance)
        )
    else:
        return render(request, "notes/create_notebook.html", {"form": form})


@method_decorator(login_required, name="dispatch")
class NotebookUpdateView(UpdateView):
    model = Notebook
    form_class = NotebookForm
    template_name = "notes/create_notebook.html"

    def get_success_url(self):
        return reverse("notebooks:notes_list", args=[self.kwargs.get("pk")])
