# Generated by Django 5.0.4 on 2024-11-26 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibreflixApp', '0009_avaliacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='estrelas',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
