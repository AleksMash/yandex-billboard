# Generated by Django 4.2 on 2023-05-01 16:29

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0012_alter_place_description_short"),
    ]

    operations = [
        migrations.AlterField(
            model_name="place",
            name="description_long",
            field=tinymce.models.HTMLField(blank=True, verbose_name="Полное описание"),
        ),
        migrations.AlterField(
            model_name="place",
            name="description_short",
            field=models.TextField(blank=True, verbose_name="Краткое описание"),
        ),
    ]