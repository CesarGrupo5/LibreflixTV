# Generated by Django 5.0.4 on 2024-11-19 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibreflixApp', '0006_episodio_descricao_episodio_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obra',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
    ]