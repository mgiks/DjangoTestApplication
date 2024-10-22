# Generated by Django 4.2 on 2024-10-22 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(max_length=255)),
                ('number_of_members', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('house_address', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('family', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='one_to_one.family')),
            ],
        ),
    ]