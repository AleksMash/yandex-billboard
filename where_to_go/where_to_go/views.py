from django.http import HttpResponse
from django.template import loader

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
                'detailsUrl': None
            }
        }
        features.append(feature)
    context['json']['features'] = features
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)