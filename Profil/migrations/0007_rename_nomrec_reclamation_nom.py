# Generated by Django 4.2 on 2023-06-10 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profil', '0006_reclamation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reclamation',
            old_name='nomRec',
            new_name='nom',
        ),
    ]
