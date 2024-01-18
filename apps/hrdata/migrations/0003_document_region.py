# Generated by Django 4.2.5 on 2023-11-15 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("hrdata", "0002_region"),
    ]

    operations = [
        migrations.AddField(
            model_name="document",
            name="region",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="hrdata.region",
            ),
        ),
    ]