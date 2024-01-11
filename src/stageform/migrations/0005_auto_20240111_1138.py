# Generated by Django 3.1.6 on 2024-01-11 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stageform', '0004_auto_20240111_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='effectuer',
            name='annee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stageform.annees'),
        ),
        migrations.AlterField(
            model_name='effectuer',
            name='code_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stageform.typedestages'),
        ),
    ]