from django.db import models
from EnterprisesApp.models import Enterprise


class Account(models.Model):
    username = models.CharField(max_length = 60, unique=True)
    password = models.CharField(max_length = 40)
    enterprise_id = models.ForeignKey(Enterprise, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username
