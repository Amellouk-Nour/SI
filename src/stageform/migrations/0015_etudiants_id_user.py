# Generated by Django 3.1.6 on 2024-01-11 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stageform', '0014_remove_etudiants_id_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiants',
            name='id_user',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
    ]
