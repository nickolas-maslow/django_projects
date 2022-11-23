from django.db import models


class ToDoList(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=False)

    def __str__(self):
        return self.name
