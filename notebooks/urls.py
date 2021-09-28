from django.urls import path

from . import views

app_name = "notebooks"

urlpatterns = [
    path("<str:pk>/notes", views.NoteListView.as_view(), name="notes_list"),
    path("create", views.notebook_create_popup, name="create_notebook"),
    path("<str:pk>/update", views.NotebookUpdateView.as_view(), name="update_notebook"),
]
