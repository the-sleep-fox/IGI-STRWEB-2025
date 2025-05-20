from django.db import models
from django.db.models import Model


# Create your models here.
class Reviews(models.Model):
    anons = models.CharField("Short review", max_length=250)
    full_text = models.TextField('Review full text')
    date = models.DateTimeField('Publish date')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"