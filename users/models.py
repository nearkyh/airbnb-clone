from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom User Model"""

    GENDER_MALE = "M"
    GENDER_FEMALE = "W"
    GENDERS = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    )
    LANGUAGE_ENGLISH = "eng"
    LANGUAGE_KOREAN = "kor"
    LANGUAGES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean"),
    )
    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"
    CURRENCIES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW"),
    )

    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(choices=GENDERS, max_length=10, blank=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(
        choices=LANGUAGES, max_length=10, blank=True, default=LANGUAGE_KOREAN
    )
    currency = models.CharField(
        choices=CURRENCIES, max_length=3, blank=True, default=CURRENCY_KRW
    )
    superhost = models.BooleanField(default=False)
