# Generated by Django 5.0.1 on 2024-03-31 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eduprod', '0003_savedflashcards_delete_savedquestion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='savedflashcards',
            old_name='flashcards',
            new_name='flashcard',
        ),
    ]