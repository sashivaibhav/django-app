# Generated by Django 4.2.5 on 2023-12-19 03:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0011_alter_chatlog_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="chatlog",
            old_name="dislike_comment",
            new_name="comment",
        ),
    ]