# Generated by Django 4.1.6 on 2023-06-05 20:34

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
