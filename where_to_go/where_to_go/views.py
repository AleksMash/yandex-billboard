from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse

from places.models import Place


def show_main(request):
    template = loader.get_template('index.html')
    context={
        'json': {
            'type':'FeatureCollection',
            'features': []
        }
    }
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
    context['json']['features'] = features
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


def get_place_details(request, id):
    place = get_object_or_404(Place, pk=id)
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