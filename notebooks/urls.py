from django.urls import path

from . import views

app_name = "notebooks"

urlpatterns = [
    path("<str:pk>/notes", views.NoteListView.as_view(), name="notes_list"),
]
