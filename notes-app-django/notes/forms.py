from django.forms import ModelForm
from django import forms
from .models import Note

class NoteForm(ModelForm):
        class Meta:
             model = Note
             fields = ('note_title', 'note_text', )

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['note_text'].widget.attrs.update({
                                                        'class': 'add_form_textarea',
                                                        'placeholder': 'What\'s on your mind ?',
                                                    })

            self.fields['note_title'].widget.attrs.update({
                                                        'class': 'add_form_title',
                                                        'placeholder': 'Title',
                                                    })

class NoteEditForm(ModelForm):
        class Meta:
             model = Note
             fields = ('note_title', 'note_text', )

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['note_text'].widget.attrs.update({
                                                        'class': 'add_form_textarea',
                                                        'placeholder': 'What\'s on your mind ?',
                                                    })

            self.fields['note_title'].widget.attrs.update({
                                                        'class': 'add_form_title',
                                                        'placeholder': 'Title',
                                                    })
