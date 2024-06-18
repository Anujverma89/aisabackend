# Generated by Django 4.2.13 on 2024-06-14 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aisapis", "0015_alter_members_image_alter_members_post_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="events",
            name="eventType",
            field=models.CharField(
                choices=[
                    ("NTE", "Non Technical Events"),
                    ("CDE", "Carrier Development Events"),
                    ("TE", "Technical Events"),
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
                    ("p", "president"),
                    ("treasurer", "Treasurers"),
                    ("tech", "Technical Team"),
                    ("vp", "Vice President"),
                    ("planning", "Planning Team"),
                    ("volunteers", "Volunteers"),
                    ("media", "Media Team"),
                    ("mentors", "mentors"),
                    ("secretary", "Secretaries"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="members",
            name="year",
            field=models.CharField(
                choices=[
                    ("SY", "Second Year"),
                    ("Final", "Final Year"),
                    ("TY", "Third Year"),
                ],
                max_length=200,
            ),
        ),
    ]