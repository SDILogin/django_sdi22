from django.db import models


class Note(models.Model):
    title = models.TextField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return (self.title if self.title else '') + \
            ' [' + (self.description[:200] if self.description else '') + ']'
