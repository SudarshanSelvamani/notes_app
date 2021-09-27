from django import forms

from notes.models import Note, Notebook


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "body", "notebook", "tag"]
        widgets = {
            "body": forms.Textarea(attrs={"rows": 20, "cols": 60}),
        }
