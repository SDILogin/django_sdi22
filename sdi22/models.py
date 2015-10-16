from django.db import models

class Note(models.Model):
    title = models.TextField(max_length=200)
    description = models.TextField()
