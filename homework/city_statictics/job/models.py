from django.db import models


class Job(models.Model):
    name = models.CharField('Job name', max_length=128, unique=True)
    description = models.TextField('Description', blank=True)
    type_of_job = models.ForeignKey('JobType', blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class JobType(models.Model):
    type = models.CharField('Job type', max_length=128, unique=True)

    def __str__(self):
        return self.type

