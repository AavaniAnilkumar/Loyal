# Generated by Django 4.2.7 on 2023-12-08 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("App1", "0041_delete_accesstoken"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CustomUser",
        ),
    ]