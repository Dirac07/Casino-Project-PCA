# Generated by Django 4.0.6 on 2022-07-19 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jugadores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugador',
            name='apuesta',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
