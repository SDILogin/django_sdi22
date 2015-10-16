from django.contrib import admin
from sdi22.models import Note

class NoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Note, NoteAdmin)
