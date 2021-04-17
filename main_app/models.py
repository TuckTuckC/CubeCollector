from django.db import models

from django.urls import reverse

class Cube(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"cube_id": self.id})
    

class Time(models.Model):
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f'{self.time} on {self.date}'