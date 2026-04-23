from django.db import models

class Enclosures(models.Model):
    description = models.CharField(max_length=500)
    size = models.DecimalField(max_digits=8, decimal_places=0)

    def __str__(self):
        return self.description

class Animals(models.Model):
    name = models.CharField(max_length=260)
    species = models.CharField(max_length=500)
    age = models.CharField(max_length=60)
    health = models.CharField(max_length=100)
    enclosure_id = models.ForeignKey(Enclosures, on_delete=models.CASCADE)

    def __str__(self):
        return self.name