# Generated by Django 4.2.5 on 2023-10-31 11:13

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_follow"),
    ]

    operations = [
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
                (
                    "location",
                    models.CharField(
                        max_length=500, verbose_name=django.contrib.auth.models.User
                    ),
                ),
                (
                    "github",
                    models.URLField(
                        max_length=1000, verbose_name=django.contrib.auth.models.User
                    ),
                ),
                (
                    "linkedin",
                    models.URLField(
                        max_length=1000, verbose_name=django.contrib.auth.models.User
                    ),
                ),
                (
                    "website",
                    models.URLField(
                        max_length=500, verbose_name=django.contrib.auth.models.User
                    ),
                ),
                (
                    "eemail",
                    models.URLField(
                        max_length=100, verbose_name=django.contrib.auth.models.User
                    ),
                ),
                (
                    "biography",
                    models.CharField(
                        max_length=150, verbose_name=django.contrib.auth.models.User
                    ),
                ),
                (
                    "about",
                    models.CharField(
                        max_length=200, verbose_name=django.contrib.auth.models.User
                    ),
                ),
            ],
            options={
                "db_table": "ProfileDetails",
            },
        ),
    ]
