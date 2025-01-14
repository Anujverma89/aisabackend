# Generated by Django 4.2.13 on 2024-06-14 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aisapis", "0004_alter_events_eventtype_alter_members_branch_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="events",
            name="eventType",
            field=models.CharField(
                choices=[
                    ("CDE", "Carrier Development Events"),
                    ("NTE", "Non Technical Events"),
                    ("TE", "Technical Events"),
                ],
                max_length=200,
            ),
        ),
        migrations.AlterField(
            model_name="members",
            name="post",
            field=models.CharField(
                choices=[
                    ("planning", "Planning Team"),
                    ("volunteers", "Volunteers"),
                    ("treasurer", "Treasurers"),
                    ("media", "Media Team"),
                    ("vp", "Vice President"),
                    ("tech", "Technical Team"),
                    ("secretary", "Secretaries"),
                    ("p", "president"),
                ],
                max_length=100,
            ),
        ),
    ]
