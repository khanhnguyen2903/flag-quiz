from django.db import models


class Flag(models.Model):
    country_name = models.CharField(
        max_length=100,
        verbose_name="Tên nước"
    )

    capital_name = models.CharField(
        max_length=100,
        verbose_name="Tên thủ đô"
    )

    continent = models.CharField(
        max_length=50,
        verbose_name="Châu lục"
    )

    url_flag = models.CharField(
        max_length=255,
        verbose_name="URL quốc kỳ"
    )

    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name = "Quốc gia"
        verbose_name_plural = "Các quốc gia"
        ordering = ["country_name"]


