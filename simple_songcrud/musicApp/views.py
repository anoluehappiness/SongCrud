from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
# Create your views here.

 #CRUD operations

class ListArtiste(generics.ListAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer

class ListSong(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class DetailSong(generics.RetrieveUpdateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer 

class DeleteSong(generics.DestroyAPIView):
    queryset = Song.objects.all() #delete
    serializer_class = SongSerializer 

class ListLyric(generics.ListAPIView):
    queryset =Lyric.objects.all() #read
    serializer_class = LyricSerializer

class DeleteLyric(generics.DestroyAPIView):
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer          
# Create your views here.
