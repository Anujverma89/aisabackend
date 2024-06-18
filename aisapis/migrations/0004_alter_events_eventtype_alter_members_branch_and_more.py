# Generated by Django 4.2.13 on 2024-06-14 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aisapis", "0003_alter_members_branch_alter_members_post"),
    ]

    operations = [
        migrations.AlterField(
            model_name="events",
            name="eventType",
            field=models.CharField(
                choices=[
                    ("TE", "Technical Events"),
                    ("NTE", "Non Technical Events"),
                    ("CDE", "Carrier Development Events"),
                ],
                max_length=200,
            ),
        ),
        migrations.AlterField(
            model_name="members",
            name="branch",
            field=models.CharField(
                choices=[("AIML", "AIML"), ("AIDS", "AIDS")], max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="members",
            name="post",
            field=models.CharField(
                choices=[
                    ("secretary", "Secretaries"),
                    ("p", "president"),
                    ("tech", "Technical Team"),
                    ("planning", "Planning Team"),
                    ("media", "Media Team"),
                    ("treasurer", "Treasurers"),
                    ("volunteers", "Volunteers"),
                    ("vp", "Vice President"),
                ],
                max_length=100,
            ),
        ),
    ]