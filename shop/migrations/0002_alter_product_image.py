# Generated by Django 4.1.4 on 2022-12-30 12:39

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=sorl.thumbnail.fields.ImageField(
                default="media/default.png", upload_to="products", verbose_name="Image"
            ),
        ),
    ]
