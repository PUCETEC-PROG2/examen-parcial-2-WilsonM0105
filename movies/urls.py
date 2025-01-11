from django.urls import path

from . import views

app_name = 'movies'

urlpatterns = [
    path("", views.index, name="index"), 
    path("movie/<int:pk>/", views.movie_detail, name="movie_detail"),
]
