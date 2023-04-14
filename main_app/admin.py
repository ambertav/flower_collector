from django.contrib import admin

from .models import Flower, Watering, Pollinator

# Register your models here.

admin.site.register([Flower, Watering, Pollinator])
