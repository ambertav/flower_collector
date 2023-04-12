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
