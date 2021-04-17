from django.db import models

class Cube(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name