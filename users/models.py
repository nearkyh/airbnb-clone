from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom User Model"""

    GENDERS = (
        ("M", "Male"),
        ("W", "Female"),
    )
    LANGUAGES = (
        ("eng", "English"),
        ("kor", "Korean"),
    )
    CURRENCIES = (
        ("usd", "USD"),
        ("krw", "KRW"),
    )

    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(choices=GENDERS, max_length=10, blank=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGES, max_length=10, blank=True)
    currency = models.CharField(choices=CURRENCIES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)
