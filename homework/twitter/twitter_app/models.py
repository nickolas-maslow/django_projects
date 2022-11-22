from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    login = models.CharField(name='login', max_length=128, unique=True)
    password = models.CharField(name='password', max_length=128)

    def __str__(self):
        return self.login