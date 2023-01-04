# Generated by Django 4.1.4 on 2023-01-04 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_alter_account_postal_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="postal_address",
            field=models.CharField(
                blank=True, max_length=50, verbose_name="Postal Address"
            ),
        ),
    ]