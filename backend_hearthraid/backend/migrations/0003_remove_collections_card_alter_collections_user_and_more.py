# Generated by Django 5.0.4 on 2024-05-03 14:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_alter_collections_card'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collections',
            name='card',
        ),
        migrations.AlterField(
            model_name='collections',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User collection owner'),
        ),
        migrations.AddField(
            model_name='collections',
            name='card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.cards', verbose_name='User collection owner'),
        ),
    ]
