# Generated by Django 4.1.5 on 2023-02-03 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("teams", "0003_alter_team_titles"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="titles",
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]