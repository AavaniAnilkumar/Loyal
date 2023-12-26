# Generated by Django 4.2.7 on 2023-12-06 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App1", "0014_token_delete_userprofile"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Token",
        ),
        migrations.AddField(
            model_name="user",
            name="last_login",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="last login"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=128, verbose_name="password"),
        ),
    ]
