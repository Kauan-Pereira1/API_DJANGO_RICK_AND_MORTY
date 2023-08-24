from django.db import models
from django.utils import timezone
# Create your models here.
    
class Location(models.Model) :
    name = models.CharField(max_length=200, null=False)
    type = models.CharField(max_length=200, null=False)
    dimension = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(default = timezone.now())
    url = models.CharField(max_length=4000)
    def __str__(self):
        return self.name
    
class Episode(models.Model) :
    name = models.CharField(max_length=200, null=False)
    air_date = models.DateTimeField(default = timezone.now())
    episodeCode = models.CharField(max_length=500, null=True)
    caracteristicas = models.CharField(max_length=1000, null=True)
    def __str__(self):
        return self.name

class Character(models.Model) :
    Name = models.CharField(max_length=200, null=False)
    status = models.CharField(max_length=200, null=True)
    species = models.CharField(max_length=200, null=False)
    type = models.CharField(max_length=200, null=False)
    gender = models.CharField(max_length=100, null=False)
    origin = models.ForeignKey(Location, related_name="origin", on_delete=models.CASCADE)
    location = models.ForeignKey(Location, related_name="location", on_delete=models.CASCADE)
    episodio = models.ForeignKey(Episode, related_name="episode", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
    
    
