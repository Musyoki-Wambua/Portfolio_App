# Generated by Django 4.2.5 on 2023-09-12 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='decsription',
            new_name='description',
        ),
    ]
