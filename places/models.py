from django.db import models

class Place(models.Model):
    title = models.CharField(
        "Название места",
        max_length=100
    )

    description_short = models.CharField(
        "Короткое описание",
        max_length=300
    )

    description_long = models.TextField(
        "Подробное описание"
    )

    longitude = models.FloatField(
        "Долгота"
    )

    latitude = models.FloatField(
        "Широта"
    )

    def __str__(self):
        return self.title