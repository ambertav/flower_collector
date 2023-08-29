from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Flower (models.Model) :

    STAGES = (
        ('S', 'Seed'),
        ('G', 'Germination'),
        ('F', 'Flowering'),
        ('P', 'Pollination'),
    )

    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    stage = models.CharField(max_length=1, choices=STAGES, default=STAGES[0][0])

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__ (self) :
        return self.name
    
    def get_absolute_url (self) :
        return reverse('flower_detail', kwargs = {'pk': self.id})
    

class Pollinator (models.Model) :

    TYPES = (
        ('Be', 'Bumblebee'),
        ('Wa', 'Wasp'),
        ('Bu', 'Butterfly'),
        ('Mo', 'Moth'),
        ('Fl', 'Fly'),
        ('Bi', 'Bird')
    )

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    type = models.CharField(max_length=2, choices=TYPES, default=TYPES[0][0])

    flowers = models.ManyToManyField(Flower)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__ (self) :
        return self.name
    
    def get_absolute_url (self) :
        return reverse('pollinator_detail', kwargs = {'pollinator_id': self.id})
    

class Watering (models.Model) :
    date = models.DateField()
    inches = models.IntegerField(default=1)

    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)

    def __str__ (self) :
        return f'{self.date}: {self.inches} of water'
    
    class Meta :
        ordering = '-date',


class Photo (models.Model) :
    url = models.CharField(max_length=250)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)

    def __str__ (self) :
        return f'Photo for flower_id: {self.flower_id} @{self.url}'