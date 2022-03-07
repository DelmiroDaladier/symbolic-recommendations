from django.contrib import admin

from recommendations.models import Movie, Review, UserProfile

admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(UserProfile)
# Register your models here.
