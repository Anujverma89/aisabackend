# Generated by Django 4.2.13 on 2024-06-14 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aisapis", "0016_alter_events_eventtype_alter_members_branch_and_more"),
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
                    ("volunteers", "Volunteers"),
                    ("planning", "Planning Team"),
                    ("tech", "Technical Team"),
                    ("vp", "Vice President"),
                    ("treasurer", "Treasurers"),
                    ("secretary", "Secretaries"),
                    ("p", "president"),
                    ("media", "Media Team"),
                    ("mentors", "Mentors"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="members",
            name="year",
            field=models.CharField(
                choices=[
                    ("Final", "Final Year"),
                    ("SY", "Second Year"),
                    ("TY", "Third Year"),
                ],
                max_length=200,
            ),
        ),
    ]