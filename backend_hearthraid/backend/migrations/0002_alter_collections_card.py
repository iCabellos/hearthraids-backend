# Generated by Django 5.0.4 on 2024-05-03 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collections',
            name='card',
            field=models.ManyToManyField(blank=True, null=True, to='backend.cards'),
        ),
    ]