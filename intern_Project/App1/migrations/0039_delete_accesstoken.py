# Generated by Django 4.2.7 on 2023-12-07 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("App1", "0038_customuser_accesstoken"),
    ]

    operations = [
        migrations.DeleteModel(
            name="AccessToken",
        ),
    ]