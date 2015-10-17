from django.shortcuts import render, get_object_or_404
from sdi22.models import Note

def index(request):
    return render(request, 'sdi22/index.html')

def notes(request):
    notes = Note.objects.all()
    context = {'notes' : notes}
    return render(request, 'sdi22/notes.html', context)

def note_description(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    context = {'note' : note}
    return render(request, 'sdi22/note_description.html', context)
