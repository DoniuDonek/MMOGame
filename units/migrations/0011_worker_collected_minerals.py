# Generated by Django 4.1.7 on 2023-02-26 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0010_alter_worker_unit_ptr'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='collected_minerals',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
