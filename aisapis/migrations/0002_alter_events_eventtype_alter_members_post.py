# Generated by Django 4.2.13 on 2024-06-14 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aisapis", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="events",
            name="eventType",
            field=models.CharField(
                choices=[
                    ("CDE", "Carrier Development Events"),
                    ("TE", "Technical Events"),
                    ("NTE", "Non Technical Events"),
                ],
                max_length=200,
            ),
        ),
        migrations.AlterField(
            model_name="members",
            name="post",
            field=models.CharField(
                choices=[
                    ("p", "president"),
                    ("media", "Media Team"),
                    ("volunteers", "Volunteers"),
                    ("secretary", "Secretaries"),
                    ("planning", "Planning Team"),
                    ("tech", "Technical Team"),
                    ("vp", "Vice President"),
                    ("treasurer", "Treasurers"),
                ],
                max_length=100,
            ),
        ),
    ]
