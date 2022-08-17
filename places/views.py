
from django.http import JsonResponse
from django.shortcuts import render

from places.models import Image, Place
from where_to_go import settings

def show_index(request):
    places_GeoJson = {
        'type': 'FeatureCollection',
        'features': []
    }

    for place in Place.objects.all():
        place_feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.longitude, place.latitude]
            },
            'properties': {
                'title': place.title,
                'placeId': place.title_id,
                'detailsUrl': f"/static/places/{place.title_id}.json"
            }
        }
        places_GeoJson['features'].append(place_feature)


    context = {'places': places_GeoJson}

    return render(request, 'index.html', context)


def show_place(request, place_id):
    place = Place.objects.get(id=place_id)
    images = Image.objects.filter(place=place)

    imgs = []

    for image in images:
        # print(image.image.url)
        # absolute_url = f"{settings.MEDIA_URL}{self.image.url}"
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

    return JsonResponse(
        place_json, 
        safe=False, 
        json_dumps_params={
            'ensure_ascii': False,
            'indent': 2
        }
    )