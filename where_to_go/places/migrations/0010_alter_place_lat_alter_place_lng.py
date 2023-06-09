# Generated by Django 4.2 on 2023-04-21 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0009_alter_place_description_long_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="place",
            name="lat",
            field=models.FloatField(null=True, verbose_name="Широта"),
        ),
        migrations.AlterField(
            model_name="place",
            name="lng",
            field=models.FloatField(null=True, verbose_name="Долгота"),
        ),
    ]
