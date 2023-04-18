# Generated by Django 4.2 on 2023-04-18 05:22

from django.db import migrations


def move_text_to_htmlfield(apps, schema_editor):
    Place = apps.get_model('places', 'Place')
    for place in Place.objects.all():
        place.description_html = place.description_long
        place.save()


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0005_place_description_html"),
    ]

    operations = [
        migrations.RunPython(move_text_to_htmlfield)
    ]
