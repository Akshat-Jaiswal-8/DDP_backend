# Generated by Django 4.1.7 on 2023-11-24 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("ddpui", "0030_orgdataflow_dataflow_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
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
                ("type", models.CharField(max_length=100)),
                ("slug", models.CharField(max_length=100)),
                ("label", models.CharField(max_length=100)),
                ("command", models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="OrgTask",
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
                    "connection_id",
                    models.CharField(max_length=36, null=True, unique=True),
                ),
                (
                    "org",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ddpui.org"
                    ),
                ),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ddpui.task"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DataflowOrgTask",
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
                    "dataflow",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ddpui.orgdataflow",
                    ),
                ),
                (
                    "orgtask",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ddpui.orgtask"
                    ),
                ),
            ],
        ),
    ]
