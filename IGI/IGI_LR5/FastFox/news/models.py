from django.db import models
from django.db.models import Model


# Create your models here.
class Articles(models.Model):
    title = models.CharField("Name", max_length=50)
    anons = models.CharField("Anons", max_length=250)
    full_text = models.TextField('Article full text')
    date = models.DateTimeField('Publish date')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Articale"
        verbose_name_plural = "Articles"