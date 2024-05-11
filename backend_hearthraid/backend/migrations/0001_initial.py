# Generated by Django 5.0.4 on 2024-05-03 13:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bases',
            fields=[
                ('base_id', models.AutoField(primary_key=True, serialize=False)),
                ('base_name', models.CharField(blank=True, max_length=128, null=True)),
                ('base_description', models.TextField(blank=True, max_length=255, null=True)),
                ('base_hp', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('card_id', models.AutoField(primary_key=True, serialize=False)),
                ('card_name', models.CharField(blank=True, max_length=128, null=True)),
                ('card_lore', models.TextField(blank=True, max_length=255, null=True)),
                ('card_power', models.IntegerField(blank=True, null=True)),
                ('card_hp', models.IntegerField(blank=True, null=True)),
                ('card_ability', models.IntegerField(blank=True, null=True)),
                ('is_legendary', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Decks',
            fields=[
                ('deck_id', models.AutoField(primary_key=True, serialize=False)),
                ('deck_name', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Heroes',
            fields=[
                ('hero_id', models.AutoField(primary_key=True, serialize=False)),
                ('hero_name', models.CharField(blank=True, max_length=128, null=True)),
                ('hero_description', models.TextField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Collections',
            fields=[
                ('collection_id', models.AutoField(primary_key=True, serialize=False)),
                ('card', models.ManyToManyField(to='backend.cards')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User collection owner')),
            ],
        ),
        migrations.AddField(
            model_name='cards',
            name='deck',
            field=models.ManyToManyField(to='backend.decks'),
        ),
        migrations.CreateModel(
            name='Expansions',
            fields=[
                ('expansion_id', models.AutoField(primary_key=True, serialize=False)),
                ('expansion_name', models.CharField(blank=True, max_length=128, null=True)),
                ('expansion_lore', models.TextField(blank=True, max_length=255, null=True)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.cards', verbose_name='Expansion from card')),
            ],
        ),
        migrations.AddField(
            model_name='decks',
            name='heroes',
            field=models.ManyToManyField(to='backend.heroes'),
        ),
        migrations.CreateModel(
            name='HeroesAbilities',
            fields=[
                ('hero_ability_id', models.AutoField(primary_key=True, serialize=False)),
                ('hero_ability_name', models.CharField(blank=True, max_length=128, null=True)),
                ('hero_ability_description', models.TextField(blank=True, max_length=255, null=True)),
                ('hero_linked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.heroes', verbose_name='Hero active ability')),
            ],
        ),
    ]
