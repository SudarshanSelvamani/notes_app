from notes.models import Notebook
from django.views.generic import ListView
from django.db.models import Count

from notes.models import Notebook


class NotebookListView(ListView):
    model = Notebook
    paginate_by = 9
    context_object_name = "notebooks"
    template_name = "notes/notebook_list.html"

    def get_queryset(self):
        return Notebook.objects.annotate(Count("note"))
