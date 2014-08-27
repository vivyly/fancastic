from django.db import models
from common.models import BaseModel
#from pictures.models import Picture

class Actor(BaseModel):
    fullname    = models.CharField(max_length=100)
    height      = models.CharField(max_length=10, blank=True)
    is_alive    = models.BooleanField(default=True)
    is_active   = models.BooleanField(default=True)
    birthday    = models.IntegerField(blank=True, null=True)
    birthmonth  = models.IntegerField(blank=True, null=True)
    birthyear   = models.IntegerField(blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True)
    url         = models.URLField(blank=True)
    #picture    = models.ForeignKey(Picture, null=True))


class Role(models.Model):
    actor       = models.ForeignKey(Actor)
    media_title = models.CharField(max_length=255)
    media_type  = models.CharField(max_length=100, blank=True)
    year        = models.IntegerField(blank=True, null=True)
    character   = models.CharField(max_length=100)
    desc        = models.TextField(blank=True)
    url         = models.URLField(blank=True)
    #picture     = models.ForeignKey(Picture, null=True)


