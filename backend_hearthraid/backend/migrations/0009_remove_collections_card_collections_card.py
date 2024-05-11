# Generated by Django 5.0.4 on 2024-05-03 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_remove_cards_card_ability'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collections',
            name='card',
        ),
        migrations.AddField(
            model_name='collections',
            name='card',
            field=models.ManyToManyField(blank=True, null=True, to='backend.cards'),
        ),
    ]
