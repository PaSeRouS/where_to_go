from django.db import models
from tinymce.models import HTMLField

class Place(models.Model):
    title = models.CharField(
        "Название места",
        max_length=100
    )

    description_short = models.CharField(
        "Короткое описание",
        max_length=300
    )

    description_long = HTMLField(
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

class Image(models.Model):
    image = models.ImageField(
        "Картинка"
    )

    image_id = models.IntegerField(
        "Позиция",
        default=0,
        db_index=True
    )

    place = models.ForeignKey(
        'Place',
        verbose_name='Место',
        related_name='images',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["image_id"]

    def __str__(self):
        return f"{self.place}, изображение №{self.image_id}"