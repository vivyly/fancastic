from django.db import models

class BaseModel(models.Model):
    slug    = models.SlugField(unique=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    creator = models.ForeignKey('fan.FanUser')
    ip      = models.IPAddressField()
