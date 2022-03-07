from email import message
from django.shortcuts import redirect, render

from .forms import ReviewForm
from .utils import get_scores
from .models import Movie, UserProfile, Review

# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')

    profile = UserProfile.objects.filter(pk=request.user.id)
    if not profile:
        movies = Movie.objects.all()[0:10]
        message = 'Currently you have no reviews. Help us to understand your movie taste better!'
        return render(request, 'recommendations/home.html', {"user": request.user, "movies": movies, "message": message})
    profile = profile[0].profile
    ids = [item.movie.movie_id for item in Review.objects.all()]

    movies = Movie.objects.all().exclude(movie_id__in=ids)

    movies = get_scores(profile, movies)
    return render(request, 'recommendations/home.html', {"user": request.user, "movies": movies})


def new_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            movie = form.cleaned_data['movie']
            rating = form.cleaned_data['rating']
            review = Review(user=user, movie=movie, rating=rating)
            review.save()
    else:
        form = ReviewForm()

    return render(request, 'recommendations/new_review.html', {"form": form})