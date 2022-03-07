from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    movie_title = models.CharField(max_length=500, default='dafault title')
    sysnopsis = models.TextField(max_length=1000)
    symbolic_synopsis = models.JSONField(null=True)
    actors = models.JSONField()
    symbolic_actors = models.JSONField(null=True)
    movie_genres = models.JSONField()
    symbolic_movie_genres = models.JSONField(null=True)
    director = models.TextField(max_length=100)
    symbolic_director = models.JSONField(null=True)

    def __str__(self):
        return self.movie_title

class Review(models.Model):
    RATING_CHOICES = [
        ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')
        ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.CharField(max_length=1, choices=RATING_CHOICES)

    def __str__(self):
        return self.movie.movie_title

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.JSONField()