from django import forms
from django.db.models import fields


from notes.models import Note, Notebook


class NotebookForm(forms.ModelForm):
    class Meta:
        model = Notebook
        fields = ["name"]
