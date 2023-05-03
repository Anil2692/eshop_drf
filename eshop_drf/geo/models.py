from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=32, unique=True)
    code = models.CharField(max_length=3, unique=True)

    class Meta:
        verbose_name_plural = 'Countries'
        ordering = ['name', ]

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=32)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=32)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



