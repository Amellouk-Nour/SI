# Generated by Django 3.1.6 on 2024-01-11 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stageform', '0010_etudiants_id_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiants',
            name='id_user',
            field=models.IntegerField(default=1),
        ),
    ]
