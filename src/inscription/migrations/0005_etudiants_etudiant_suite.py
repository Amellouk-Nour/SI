# Generated by Django 3.1.6 on 2024-01-10 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0004_annees_etudiants_promos'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiants',
            name='etudiant_suite',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]