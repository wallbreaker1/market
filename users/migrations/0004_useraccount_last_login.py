# Generated by Django 4.1.1 on 2022-10-16 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_useraccount_table"),
    ]

    operations = [
        migrations.AddField(
            model_name="useraccount",
            name="last_login",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="last login"
            ),
        ),
    ]