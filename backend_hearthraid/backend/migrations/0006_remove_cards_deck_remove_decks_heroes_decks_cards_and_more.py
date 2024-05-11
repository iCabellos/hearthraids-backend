# Generated by Django 5.0.4 on 2024-05-03 14:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_remove_expansions_card_cards_expansion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cards',
            name='deck',
        ),
        migrations.RemoveField(
            model_name='decks',
            name='heroes',
        ),
        migrations.AddField(
            model_name='decks',
            name='cards',
            field=models.ManyToManyField(blank=True, null=True, to='backend.cards'),
        ),
        migrations.AddField(
            model_name='decks',
            name='hero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.heroes', verbose_name='Main Hero deck'),
        ),
    ]
