# Generated by Django 4.1.7 on 2023-02-21 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0007_race_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='flying_unit',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('attack', models.PositiveIntegerField(default=5)),
                ('defence', models.PositiveIntegerField(default=0)),
                ('speed', models.PositiveIntegerField(default=10)),
                ('health', models.PositiveIntegerField(default=50)),
                ('description', models.TextField(max_length=1000)),
                ('photo', models.ImageField(upload_to='')),
                ('mineral_cost', models.PositiveIntegerField(default=0)),
                ('gas_cost', models.PositiveIntegerField(default=0)),
                ('capacity', models.PositiveIntegerField(default=1)),
                ('anti_air', models.BooleanField(default=False)),
                ('flying_unit', models.BooleanField(default=False)),
                ('race', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='units.race')),
            ],
        ),
    ]