from django.db import models
from django.db import models


class Human(models.Model):
    age = models.IntegerField(
        verbose_name='height',
        editable=True,
        blank=False
    )
    name = models.CharField(
        verbose_name='name',
        editable=True,
        blank=False,
        max_length=120
    )


class Child(models.Model):
    age = models.IntegerField(
        verbose_name='height',
        editable=True,
        blank=False
    )
    name = models.CharField(
        verbose_name='name',
        editable=True,
        blank=False,
        max_length=120
    )


class Icecream(models.Model):
    price = models.IntegerField(
        verbose_name='height',
        editable=True,
        blank=False,
    )
    label = models.CharField(
        verbose_name='name',
        editable=True,
        blank=False,
        max_length=120
    )


class IcecreamShop(models.Model):
    assortment = models.IntegerField(
        verbose_name='height',
        editable=True,
        blank=False
    )
    brand = models.CharField(
        verbose_name='name',
        editable=True,
        blank=False,
        max_length=120
    )
