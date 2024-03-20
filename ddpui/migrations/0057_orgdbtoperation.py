# Generated by Django 4.1.7 on 2024-02-28 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("ddpui", "0056_remove_orgdbtmodel_config_orgdbtmodel_output_cols"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrgDbtOperation",
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
                ("uuid", models.UUIDField(editable=False, unique=True)),
                ("seq", models.IntegerField(default=0)),
                ("output_cols", models.JSONField(default=list)),
                ("config", models.JSONField(null=True)),
                (
                    "dbtmodel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ddpui.orgdbtmodel",
                    ),
                ),
            ],
        ),
    ]