# Generated by Django 4.2.13 on 2024-06-14 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aisapis", "0012_delete_members_alter_events_eventtype"),
    ]

    operations = [
        migrations.CreateModel(
            name="members",
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
                ("name", models.CharField(max_length=100)),
                (
                    "post",
                    models.CharField(
                        choices=[
                            ("vp", "Vice President"),
                            ("p", "president"),
                            ("planning", "Planning Team"),
                            ("tech", "Technical Team"),
                            ("treasurer", "Treasurers"),
                            ("media", "Media Team"),
                            ("secretary", "Secretaries"),
                            ("volunteers", "Volunteers"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "branch",
                    models.CharField(
                        choices=[("AIML", "AIML"), ("AIDS", "AIDS")], max_length=100
                    ),
                ),
                (
                    "year",
                    models.CharField(
                        choices=[
                            ("Final", "Final Year"),
                            ("TY", "Third Year"),
                            ("SY", "Second Year"),
                        ],
                        max_length=200,
                    ),
                ),
                ("contact", models.CharField(max_length=10)),
                ("image", models.ImageField(upload_to="member")),
            ],
        ),
        migrations.AlterField(
            model_name="events",
            name="eventType",
            field=models.CharField(
                choices=[
                    ("NTE", "Non Technical Events"),
                    ("TE", "Technical Events"),
                    ("CDE", "Carrier Development Events"),
                ],
                max_length=200,
            ),
        ),
    ]
