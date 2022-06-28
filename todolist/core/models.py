from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    # def __str__(self):
    #     return self.slug
