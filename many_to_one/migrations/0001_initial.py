# Generated by Django 4.2 on 2024-10-22 23:06

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('revenue', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('number_plate', models.IntegerField()),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='many_to_one.manufacturer')),
            ],
        ),
    ]
