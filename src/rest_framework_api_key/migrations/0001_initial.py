# Generated by Django 2.1.7 on 2019-04-03 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []  # type: ignore

    operations = [
        migrations.CreateModel(
            name="APIKey",
            fields=[
                (
                    "id",
                    models.CharField(
                        max_length=100, primary_key=True, serialize=False
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("name", models.CharField(default=None, max_length=50)),
                (
                    "revoked",
                    models.BooleanField(
                        blank=True,
                        default=False,
                        help_text=(
                            "If the API key is revoked, clients cannot use it anymore."
                        ),
                    ),
                ),
            ],
            options={
                "verbose_name": "API key",
                "verbose_name_plural": "API keys",
                "ordering": ("-created",),
            },
        )
    ]
