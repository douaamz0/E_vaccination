# Generated by Django 4.2 on 2023-06-11 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profil', '0007_rename_nomrec_reclamation_nom'),
    ]

    operations = [
        migrations.AddField(
            model_name='membreequipe',
            name='equipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Profil.equipemedicale'),
        ),
    ]