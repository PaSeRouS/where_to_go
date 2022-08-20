
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places.models import Image, Place
from where_to_go import settings

def show_index(request):
    places_GeoJson = {
        'type': 'FeatureCollection',
        'features': []
    }

    for place in Place.objects.all():
        place_json = serialize_place(place)

        place_feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.longitude, place.latitude]
            },
            'properties': {
                'title': place.title,
                'placeId': place.title,
                'detailsUrl': reverse('place_id', kwargs={'place_id':place.id})
            }
        }
        places_GeoJson['features'].append(place_feature)


    context = {'places': places_GeoJson}

    return render(request, 'index.html', context)


def show_place(request, place_id):
    place = get_object_or_404(Place, id=place_id)

    place_json = serialize_place(place)

    return JsonResponse(
        place_json, 
        safe=False, 
        json_dumps_params={
            'ensure_ascii': False,
            'indent': 2
        }
    )

def serialize_place(place):
    images = Image.objects.filter(place=place)

    imgs = []

    for image in images:
        imgs.append(image.image.url)

    place_json = {
        "title": place.title,
        "imgs": imgs,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.longitude,
            "lat": place.latitude
        }
    }

    return place_json