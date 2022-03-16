from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'note_title', 'pub_date')

admin.site.register(Note, NoteAdmin)
