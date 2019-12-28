from django.urls import path,include
from api import views


urlpatterns = [
    path('search/',views.SearchByNameApi.as_view()),
    path("movie_search/", views.SearchByImdbIdApi.as_view(), name="imdb")
]
