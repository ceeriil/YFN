# Generated by Django 4.2.5 on 2023-10-08 16:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="postmodel",
            options={"ordering": ("-date_created",)},
        ),
    ]
