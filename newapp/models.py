from django.db import models

# Create your models here.
class Produs (models.Model):
    title = models.CharField(max_length=255)
    pret = models.IntegerField
    cantitate = models.IntegerField

    owner = models.ForeignKey("auth.User", models.CASCADE, null=True, blank=True)

