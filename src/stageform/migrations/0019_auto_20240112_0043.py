# Generated by Django 3.1.6 on 2024-01-11 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stageform', '0018_auto_20240112_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stages',
            name='fiche_évaluation',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]