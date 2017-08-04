from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    first_name = models.CharField(max_length = 60, unique=True)
    mobile_number = models.CharField(max_length = 40)
    user = models.OneToOneField(
        User,
        primary_key=True,
        related_name='profile')

    class Meta:
        verbose_name_plural = 'User Profiles'