from django.db import models

class City(models.Model):
    title = models.CharField("Название города", max_length=50)

    class Meta:
        ordering = ["title"]
        verbose_name = "Город"
        verbose_name_plural = "Города"
    
    def __str__(self) -> str:
        return self.title