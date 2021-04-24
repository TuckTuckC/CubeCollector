from django.db import models

from django.urls import reverse


class Stand(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    # Other goodness such as 'def __str__():' below
    def __str__(self):
        return f'{self.name} {self.color}'

    # Add this method
    def get_absolute_url(self):
        return reverse('stand_detail', kwargs={'stand_id': self.id})

class Cube(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    stands = models.ManyToManyField(Stand)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"cube_id": self.id})
    

class Time(models.Model):
    date = models.DateField('Solve Date')
    time = models.TimeField()

    cube = models.ForeignKey(Cube, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.time}'

    class Meta:
        ordering = ['time']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    cube = models.ForeignKey(Cube, on_delete=models.CASCADE)

    def __str__(self):
        return f'Photo for cube_id: {self.cube_id} @{self.url}'