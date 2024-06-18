# Generated by Django 4.2.13 on 2024-06-14 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aisapis", "0002_alter_events_eventtype_alter_members_post"),
    ]

    operations = [
        migrations.AlterField(
            model_name="members",
            name="branch",
            field=models.CharField(
                choices=[("AIDS", "AIDS"), ("AIML", "AIML")], max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="members",
            name="post",
            field=models.CharField(
                choices=[
                    ("tech", "Technical Team"),
                    ("media", "Media Team"),
                    ("secretary", "Secretaries"),
                    ("treasurer", "Treasurers"),
                    ("volunteers", "Volunteers"),
                    ("planning", "Planning Team"),
                    ("p", "president"),
                    ("vp", "Vice President"),
                ],
                max_length=100,
            ),
        ),
    ]