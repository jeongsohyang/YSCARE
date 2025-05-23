from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    GENDER_CHOICES = [
        (0, 'Male'),
        (1, 'Female'),
    ]

    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.IntegerField(default=0)
    height = models.FloatField(default=0.0)
    weight = models.FloatField(default=0.0)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=0)

    REQUIRED_FIELDS = ['email', 'name', 'gender', 'age', 'height', 'weight']
    # USERNAME_FIELD는 'username' (기본값 유지)

    def __str__(self):
        return self.username
