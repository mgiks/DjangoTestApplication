# Generated by Django 4.2 on 2024-10-24 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('slug', models.SlugField(blank=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('revenue', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('number_plate', models.IntegerField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='many_to_one.manufacturer')),
            ],
        ),
    ]
