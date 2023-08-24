from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CharacterAPIView(APIView):
    def post(self,request):
        characterJson = request.data
        characterSerialized = CharacterSerializer(data=characterJson)
        characterSerialized.is_valid(raise_exception=True)
        characterSerialized.save()
        return Response(status=status.HTTP_201_CREATED,data=characterSerialized.data)
        
        
    def get(self, request, id=''):
        if id=='':
            #primeiro vamos fazer um select all do banco:
            characterFound = Character.objects.all() #select *from people;
            #agora pegamos os dados em python e mandamos p/ json
            characterSerialized = CharacterSerializer(characterFound, many=True)
            #manda a resposta para quem chamou a API:
            #Response(data="ok")
            return Response(characterSerialized.data)
        else:
            try:
                characterFound = Character.objects.get(id=id)
                characterSerialized = CharacterSerializer(characterFound)
                return Response(characterSerialized.data)
            except Character.DoesNotExist:
                return Response(status=404, data="Character Not Found!!!")
        

class LocationAPIView(APIView):
    def post(self,request):
        locationJson = request.data
        locationSerialized = LocationSerializer(data=locationJson)
        locationSerialized.is_valid(raise_exception=True)
        locationSerialized.save()
        return Response(status=status.HTTP_201_CREATED,data=locationSerialized.data)
    def get(self,request, id =''):
        if id == '':
            #primeiro vamos fazer um select all do banco:
            locationFound = Location.objects.all() #select *from Planet;
            #agora pegamos os dados em python e mandamos p/ json
            locationSerialized = LocationSerializer(locationFound, many=True)
            #manda a resposta para quem chamou a API:
            return Response(locationSerialized.data)
        else: 
            try:
                locationFound = Location.objects.get(id=id)
                locationSerialized = LocationSerializer(locationFound)
                return Response(locationSerialized.data)
            except Location.DoesNotExist:
                return Response(status=404, data="Location Not Found!!!")
        
        
class EpisodeAPIView(APIView):
    def post(self,request):
        episodeJson = request.data
        episodeSerialized = EpisodeSerializer(data =episodeJson)
        episodeSerialized.is_valid(raise_exception=True)
        episodeSerialized.save()
        return Response(status=status.HTTP_201_CREATED,data=episodeSerialized.data)
    
    def get(self, request, id=''):
        if id == '':
            #primeiro vamos fazer um select all do banco:
            episodeFound = Episode.objects.all() #select *from Starships;
            #agora pegamos os dados em python e mandamos p/ json
            episodeSerialized = EpisodeSerializer(episodeFound, many=True)
            #manda a resposta para quem chamou a API:
            return Response(episodeSerialized.data)
        else:
            try:
                episodeFound = Episode.objects.get(id=id)
                episodeSerialized = EpisodeSerializer(episodeFound)
                return Response(episodeSerialized.data)
            except Episode.DoesNotExist:
                return Response(status=404, data="Episode Not Found!!!")
    def delete(self,request, id=''):
        try:
            episodeFound = Episode.objects.get(id=id)
            episodeFound.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Episode.DoesNotExist:
            return Response(status=404, data="Episode Not Found!!!")