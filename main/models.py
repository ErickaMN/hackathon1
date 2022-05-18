from django.db import models


class Producer(models.Model):
    name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    image = models.ImageField (blank=True, null=True, upload_to='producers')


class Genre(models.Model):
    slug = models.SlugField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, unique=True)

CHOICES = (
    ('in stock', 'в наличие'),
    (' out of stock', 'нет в наличии')
)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    images = models.ImageField(blank=True, null=True, upload_to='movies')
    status = models.CharField(choices=CHOICES, max_length=100)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, related_name='movie')

