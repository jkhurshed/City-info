from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=250, verbose_name="Категория")

    class Meta:
        ordering = ["title"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    
    def __str__(self) -> str:
        return self.title

