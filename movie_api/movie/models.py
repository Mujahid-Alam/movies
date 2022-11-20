from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True)
    date_released = models.DateField() 
    price = models.IntegerField()

    def __str__(self):
        return self.title