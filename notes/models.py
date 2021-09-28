from django.db import models

from taggit.managers import TaggableManager
from model_utils.models import TimeStampedModel


class Notebook(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Note(TimeStampedModel):
    title = models.CharField(max_length=100)
    body = models.TextField()
    notebook = models.ForeignKey(
        Notebook, blank=True, null=True, on_delete=models.CASCADE
    )
    tag = TaggableManager(blank=True)

    def __str__(self):
        return self.title
