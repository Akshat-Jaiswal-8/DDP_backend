# Generated by Django 4.1.7 on 2023-03-14 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ddpui", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Invitation",
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
                ("invited_email", models.CharField(max_length=50)),
                ("invited_on", models.DateTimeField()),
                ("invite_code", models.CharField(max_length=36)),
                (
                    "invited_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ddpui.clientuser",
                    ),
                ),
            ],
        ),
    ]