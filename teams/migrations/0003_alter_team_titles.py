# Generated by Django 4.1.5 on 2023-02-03 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("teams", "0002_alter_team_fifa_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="titles",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
