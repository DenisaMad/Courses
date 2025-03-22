from django.db import models

# Create your models here.

class AnUniversitar(models.Model):
    an_start = models.IntegerField(null=False, blank=False)
    an_end = models.IntegerField(null=False, blank=False)