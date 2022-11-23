from django.db import models


class Note(models.Model):
    user = models.CharField(max_length=128, blank=False, unique=True)

    def __str__(self):
        return self.user

