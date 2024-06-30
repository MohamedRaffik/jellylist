# Generated by Django 5.0.6 on 2024-06-29 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="JellyfinServer",
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
                ("name", models.CharField(max_length=255)),
                ("url", models.URLField()),
                ("api_key", models.CharField(max_length=255)),
            ],
        ),
    ]
