# Generated by Django 4.2.5 on 2023-11-18 06:58

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SQLLog",
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
                ("question", models.TextField()),
                ("context", models.TextField()),
                ("response", models.TextField()),
                ("last_updated", models.DateTimeField(auto_now=True)),
                ("temp", models.TextField()),
            ],
        ),
    ]
