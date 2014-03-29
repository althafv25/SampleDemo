from django.db import models
from ckeditor.fields import RichTextField
from djangoratings.fields import RatingField

class Food(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return self.name


class Cuisine(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    thumbnail_image = models.ImageField(upload_to='images')
    background_image = models.ImageField(upload_to='images')

    def __unicode__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    description = RichTextField()
    rating = RatingField(range=5, can_change_vote=True, allow_anonymous=False)
    cuisines = models.ManyToManyField(Cuisine)

    def __unicode__(self):
        return self.name


