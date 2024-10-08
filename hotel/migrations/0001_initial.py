# Generated by Django 5.0.3 on 2024-04-01 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cottages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.IntegerField()),
                ("description", models.TextField()),
                ("price", models.FloatField(default=0)),
                ("status", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Rooms",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.IntegerField()),
                ("description", models.TextField()),
                ("price", models.FloatField(default=0)),
                ("status", models.BooleanField(default=False)),
            ],
        ),
    ]
