from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        "Название места",
        max_length=100,
        unique=True
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

    position = models.IntegerField(
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
        ordering = ["position"]

    def __str__(self):
        return f"{self.place}, изображение №{self.position}"
