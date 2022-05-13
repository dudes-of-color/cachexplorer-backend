from django.contrib.auth import get_user_model
from django.db import models


class Cache(models.Model):
    title = models.CharField(max_length=256, default='TITLE')
    location = models.CharField(max_length=256)
    lat = models.FloatField()
    long = models.FloatField()
    img = models.CharField(max_length=1024)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    
    def __str__(self):
        return self.title + ' located @' + self.location
