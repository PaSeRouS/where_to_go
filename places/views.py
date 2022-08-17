from django.shortcuts import render

from places.models import Image, Place

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