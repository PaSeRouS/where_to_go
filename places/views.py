from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places.models import Place


def show_index(request):
    features = [{
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [place.longitude, place.latitude]
        },
        'properties': {
            'title': place.title,
            'placeId': place.title,
            'detailsUrl': reverse(
                'place_id',
                kwargs={
                    'place_id': place.id
                }
            )
        }
    } for place in Place.objects.all()]

    place_info = {
        'type': 'FeatureCollection',
        'features': features
    }

    context = {'places': place_info}

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
    imgs = [image.image.url for image in place.images.all()]

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
