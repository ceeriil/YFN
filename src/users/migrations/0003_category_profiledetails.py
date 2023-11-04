# Generated by Django 4.2.5 on 2023-11-04 09:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_follow"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
            ],
        ),
        migrations.CreateModel(
            name="ProfileDetails",
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
                ("location", models.CharField(max_length=500)),
                ("github", models.URLField(max_length=1000)),
                ("linkedin", models.URLField(max_length=1000)),
                ("website", models.URLField(max_length=500)),
                ("eemail", models.URLField(max_length=100)),
                ("biography", models.CharField(max_length=150)),
                ("about", models.CharField(max_length=200)),
            ],
            options={
                "db_table": "ProfileDetails",
            },
        ),
    ]
