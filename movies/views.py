from django.shortcuts import render, get_object_or_404
from .models import Movie


def index(request):
    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies': movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movie_detail.html', {'movie': movie})