# Generated by Django 4.2.13 on 2024-06-14 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aisapis", "0014_alter_members_branch_alter_members_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="members",
            name="image",
            field=models.ImageField(upload_to="member"),
        ),
        migrations.AlterField(
            model_name="members",
            name="post",
            field=models.CharField(
                choices=[
                    ("vp", "Vice President"),
                    ("tech", "Technical Team"),
                    ("media", "Media Team"),
                    ("secretary", "Secretaries"),
                    ("planning", "Planning Team"),
                    ("treasurer", "Treasurers"),
                    ("volunteers", "Volunteers"),
                    ("p", "president"),
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
                    ("TY", "Third Year"),
                    ("SY", "Second Year"),
                ],
                max_length=200,
            ),
        ),
    ]