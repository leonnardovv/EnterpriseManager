from django.db import models

class Enterprise(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name
