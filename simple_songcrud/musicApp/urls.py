from django.urls import path
from .views import *

urlpatterns = [
    path("",ListArtiste.as_view()),
    path("<int:fk>/",DetailSong .as_view()),
    path("",ListSong.as_view()),
    path("delete/<int:fk>",DeleteSong.as_view()),
    path("",ListLyric.as_view()),
    path("delete/<int:fk>",DeleteLyric.as_view())
]