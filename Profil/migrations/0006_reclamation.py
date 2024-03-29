# Generated by Django 4.2 on 2023-06-10 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profil', '0005_citoyen_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reclamation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomRec', models.CharField(max_length=100)),
                ('date_reclamation', models.DateTimeField()),
                ('description', models.TextField()),
                ('symptomes', models.TextField()),
                ('date_effets_secondaires', models.DateField()),
                ('est_traitee', models.BooleanField(default=False)),
                ('date_traitement', models.DateTimeField(blank=True, null=True)),
                ('commentaire_traitement', models.TextField(blank=True, null=True)),
                ('citoyen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profil.citoyen')),
            ],
        ),
    ]
