# Generated by Django 3.1.6 on 2024-01-11 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stageform', '0013_auto_20240111_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etudiants',
            name='id_user',
        ),
    ]
