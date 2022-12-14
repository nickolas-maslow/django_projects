# Generated by Django 4.1.3 on 2022-11-26 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=128, unique=True, verbose_name='Job type')),
            ],
            options={
                'verbose_name': 'Job type',
                'verbose_name_plural': 'Job types',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Job name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('type_of_job', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='job.jobtype')),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
            },
        ),
    ]
