from django.urls import path
from .views import *

urlpatterns = [
    path("character/", CharacterAPIView.as_view(), name='character'),
    path("character/<int:id>", CharacterAPIView.as_view(), name='characterParameter'),
    path("location/", LocationAPIView.as_view(), name='location'),
    path("location/<int:id>", LocationAPIView.as_view(), name='locationParameter'),
    path("episode/", EpisodeAPIView.as_view(), name='episode'),    
    path("episode/<int:id>", EpisodeAPIView.as_view(), name='episodeParameter'),
]
