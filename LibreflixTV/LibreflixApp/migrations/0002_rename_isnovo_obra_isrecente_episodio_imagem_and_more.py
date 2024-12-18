# Generated by Django 5.0.4 on 2024-11-13 00:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibreflixApp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='obra',
            old_name='isNovo',
            new_name='isRecente',
        ),
        migrations.AddField(
            model_name='episodio',
            name='imagem',
            field=models.URLField(default='https://via.placeholder.com/150'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='obra',
            name='imagem',
            field=models.URLField(db_default='https://via.placeholder.com/150'),
        ),
        migrations.CreateModel(
            name='ContinuarAssistindo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibreflixApp.obra')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Favoritados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibreflixApp.obra')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
