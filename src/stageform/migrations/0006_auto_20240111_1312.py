# Generated by Django 3.1.6 on 2024-01-11 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stageform', '0005_auto_20240111_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professeurs',
            name='prof_tel_ecole',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]