# Generated by Django 4.1.7 on 2023-02-18 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0004_alter_unit_attack_alter_unit_defence_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='anti_air',
            field=models.BooleanField(default=False),
        ),
    ]