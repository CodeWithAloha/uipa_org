# Generated by Django 3.1.4 on 2021-02-03 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicbody', '0032_auto_20201221_1953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foilaw',
            old_name='description',
            new_name='_description',
        ),
        migrations.RenameField(
            model_name='foilaw',
            old_name='letter_end',
            new_name='_letter_end',
        ),
        migrations.RenameField(
            model_name='foilaw',
            old_name='letter_start',
            new_name='_letter_start',
        ),
        migrations.RenameField(
            model_name='foilaw',
            old_name='long_description',
            new_name='_long_description',
        ),
        migrations.RenameField(
            model_name='foilaw',
            old_name='name',
            new_name='_name',
        ),
        migrations.RenameField(
            model_name='foilaw',
            old_name='request_note',
            new_name='_request_note',
        ),
        migrations.RenameField(
            model_name='foilaw',
            old_name='slug',
            new_name='_slug',
        ),
        migrations.RenameField(
            model_name='foilaw',
            old_name='refusal_reasons',
            new_name='_refusal_reasons',
        ),
    ]
