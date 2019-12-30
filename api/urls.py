from django.urls import path,include
from api import views


urlpatterns = [
    path('search/',views.SearchByNameApi.as_view()),
    path("movie_search/", views.SearchByImdbIdApi.as_view(), name="imdb"),
    # path("upcomings/", views.UpcomingApi.as_view(), name="imdb"),
    path("movie_tags/", views.GetTags.as_view(), name="tags"),
    path("movie_search_tags/<int:g_id>/<int:page>/", views.SearchByTagApi.as_view(), name="find_tag"),
    path("ip/", views.InfoByIp.as_view(), name="ip"),
    path("address/", views.ObtainAddress.as_view(), name="address"),
    # path("url_shorten/", views.UrlShorten.as_view(), name="short_url"),
    path("country_info/<str:country>/", views.FindCountryInfo.as_view(), name="country"),
    path("weather/", views.Weather.as_view(), name="weather"),
    path("tts/<str:text>", views.TextToSpeech.as_view(), name="tts"),
    path("qr/<str:text>", views.QrGenerator.as_view(), name="qr"),
    # path("movie_search/", views.SearchByImdbIdApi.as_view(), name="imdb"),
    # path("movie_search/", views.SearchByImdbIdApi.as_view(), name="imdb"),

]
