# Generated by Django 3.1.6 on 2024-01-11 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stageform', '0016_auto_20240111_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='stages',
            name='promo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='stageform.promos'),
        ),
        migrations.AlterField(
            model_name='stages',
            name='annee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stageform.annees'),
        ),
    ]
