# Generated by Django 4.1.3 on 2022-11-28 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_alter_jobtype_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='type_of_job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='job.jobtype'),
        ),
    ]
