from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import *
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import DetailView
from django.db.models import Q


def index(request):
    notes = Note.objects.order_by('-pub_date')
    query = request.GET.get('q')

    if query:
        search_notes = Note.objects.filter(Q(note_title__icontains=query) | Q(note_text__icontains=query))
        notes = search_notes.order_by('-pub_date')

    context = {'notes': notes}

    return render(request, 'notes/index.html', context)

class NoteDetailView(DetailView):
    model = Note


def add(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'NOTE HAS BEEN CREATED')
            return redirect('home')

    else:
        form = NoteForm()

    context = {'form': form}

    return render(request, 'notes/add.html', context)

def delete(request, note_id):
    note_to_delete = get_object_or_404(Note, id=note_id)

    note_to_delete.delete()
    messages.success(request, 'NOTE HAS BEEN DELETED')
    return redirect('home')

def edit(request, id):
    note = get_object_or_404(Note, id=id)

    if request.method == 'POST':
        form = NoteEditForm(request.POST or None, instance=note)

        if form.is_valid():
            form.save()
            messages.success(request, 'NOTE HAS BEEN UPDATED')
            return redirect('home')

    else:
        form = NoteForm(instance=note)

    context = {
    'form': form,
    'note': note
    }

    return render(request, 'notes/edit.html', context)

def detail_edit(request, id):
    note = get_object_or_404(Note, id=id)

    if request.method == 'POST':
        form = NoteEditForm(request.POST or None, instance=note)

        if form.is_valid():
            form.save()
            messages.success(request, 'NOTE HAS BEEN UPDATED')
            return redirect('note_detail', id)

    else:
        form = NoteForm(instance=note)

    context = {
    'form': form,
    'note': note
    }

    return render(request, 'notes/edit.html', context)
