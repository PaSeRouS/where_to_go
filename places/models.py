from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        "Название места",
        max_length=100
    )

    description_short = models.TextField(
        "Короткое описание",
        blank=True
    )

    description_long = HTMLField(
        "Подробное описание",
        blank=True
    )

    longitude = models.FloatField(
        "Долгота"
    )

    latitude = models.FloatField(
        "Широта"
    )

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(
        "Картинка"
    )

    position_id = models.IntegerField(
        "Позиция",
        default=0
    )

    place = models.ForeignKey(
        'Place',
        verbose_name='Место',
        related_name='images',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["position_id"]

    def __str__(self):
        return f"{self.place}, изображение №{self.image_id}"
