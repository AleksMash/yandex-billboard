from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places.models import Place


def show_main(request):
    places = Place.objects.all()
    features = []
    for place in places:
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.lng, place.lat]
            },
            'properties': {
                'title': place.title,
                'place_id': place.id,
                'detailsUrl': reverse('place_details', kwargs={'id': place.id})
            }
        }
        features.append(feature)
        context = {
            'places': {
                'type': 'FeatureCollection',
                'features': features
            }
        }
    return render(request, template_name='index.html', context=context)


def get_place_details(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_serialized = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat
        }
    }
    return JsonResponse(place_serialized, json_dumps_params={'indent': 2, 'ensure_ascii': False})
