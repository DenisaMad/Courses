from django.db import models

# Create your models here.

class AnUniversitar(models.Model):
    an_start = models.IntegerField(null=False, blank=False)
    an_end = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return str(self.an_start)+"-"+str(self.an_end)