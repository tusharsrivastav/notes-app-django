import datetime

from django.db import models
from django.utils import timezone

class Note(models.Model):
    note_title = models.CharField(max_length=200, default="Untitled")
    note_text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.note_text
