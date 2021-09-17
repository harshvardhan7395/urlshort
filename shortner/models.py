from django.db import models
from django.utils.crypto import get_random_string


# Create your models here.

def generate_public_id():
    """
    Method to generate random public id which is easy to read.
    Uses only capital letters and numerals, and excludes similar looking characters like 0,O and I,L,1
    """
    return get_random_string(
        length=8, allowed_chars="ABCDEFGHJKMNPQRSTUVWXYZ23456789"
    )


class urlShortner(models.Model):
    public_key = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=True,
    )
    url = models.CharField(max_length=1000)
