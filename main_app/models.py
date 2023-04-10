from django.db import models

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

    def __str__ (self) :
        return self.name
