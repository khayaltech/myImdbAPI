from django.http import JsonResponse
from django.shortcuts import render
from .models import Movie

def movie_list(request):
  movies=Movie.objects.all().values()
  print((movies))
  context={
    'movies':list(movies)
  }
  
  return JsonResponse(context)


def movie_single(request,pk):
  movie=Movie.objects.get(id=pk)
  # context={
  #   'movie':list(movie)
  # }
  context={
    'title':movie.title,
    'description':movie.description,
    'active':movie.active
  }
  return JsonResponse(context)

