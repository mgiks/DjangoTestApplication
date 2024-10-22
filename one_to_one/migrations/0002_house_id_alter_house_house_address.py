# Generated by Django 4.2 on 2024-10-22 11:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("one_to_one", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="house",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                default=1,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="house",
            name="house_address",
            field=models.CharField(max_length=255),
        ),
    ]
