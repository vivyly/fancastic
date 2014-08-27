from django.db import models
from django.contrib.auth.models import AbstractUser

class FanUser(AbstractUser):

    """ Inherited from AbstractUser class
        Required:
        Username (30 char or fewer)
        password
        email
        ------------------------
        Other fields that are available are optional.
        first_name (max 30 char)
        last_name (max 30 char)
        is_staff (bool, default=False)
        is_active (bool, default=True)
        date_joined
        ------------------------
        manager is UserManager()
    """
    slug           = models.SlugField(unique=True)
    is_contributor = models.BooleanField(default=False)
    desc           = models.TextField(blank=True)
