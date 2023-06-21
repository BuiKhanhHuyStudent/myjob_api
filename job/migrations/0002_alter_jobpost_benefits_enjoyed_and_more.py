# Generated by Django 4.1.6 on 2023-06-05 20:44

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='benefits_enjoyed',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='job_description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='job_requirement',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
