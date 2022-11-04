from rest_framework import serializers
from .models import *

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ("first_name","last_name","age")

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ("artiste","title","date_released","likes") 

class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = ("song","content")