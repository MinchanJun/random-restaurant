from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

import misaka

from django.contrib.auth import get_user_model
User = get_user_model()

class TempRestaurant(models.Model):
    nameOfRestaurant = models.CharField(max_length=255, unique=True)
    rating = models.CharField(max_length=1, unique=True)
    address= models.CharField(max_length=128)
    city = models.CharField(max_length=64, default="Stony Brook")
    state = models.CharField(max_length=2, default="NY")
    zip_code = models.CharField(max_length=5, default="11375")
    description = models.TextField(blank=True,default='')
    description_html = models.TextField(editable=False, default='', blank=True)

    def __str__(self):
        return self.nameOfRestaurant

    class Meta:
        ordering = ['nameOfRestaurant']
