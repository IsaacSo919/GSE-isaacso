# Generated by Django 5.0.2 on 2024-03-19 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EXEplorer', '0003_userprofile_carbonfootfrint'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='coins',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='cherries',
            field=models.IntegerField(default=20),
        ),
    ]