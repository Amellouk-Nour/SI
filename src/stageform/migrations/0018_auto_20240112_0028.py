# Generated by Django 3.1.6 on 2024-01-11 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stageform', '0017_auto_20240111_1730'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entreprises',
            options={'verbose_name_plural': 'Entreprises'},
        ),
        migrations.AlterModelOptions(
            name='etudiants',
            options={'verbose_name_plural': 'Etudiants'},
        ),
        migrations.AlterModelOptions(
            name='professeurs',
            options={'verbose_name_plural': 'Professeurs'},
        ),
        migrations.AlterModelOptions(
            name='promos',
            options={'verbose_name_plural': 'Promos'},
        ),
        migrations.AlterModelOptions(
            name='stages',
            options={'verbose_name_plural': 'Stages'},
        ),
        migrations.AlterModelOptions(
            name='tuteurs',
            options={'verbose_name_plural': 'Tuteurs'},
        ),
        migrations.AddField(
            model_name='stages',
            name='fiche_évaluation',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]