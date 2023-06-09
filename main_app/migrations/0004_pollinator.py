# Generated by Django 4.1.7 on 2023-04-14 03:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0003_watering'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pollinator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=100)),
                ('type', models.CharField(choices=[('Be', 'Bumblebee'), ('Wa', 'Wasp'), ('Bu', 'Butterfly'), ('Mo', 'Moth'), ('Fl', 'Fly'), ('Bi', 'Bird')], default='Be', max_length=2)),
                ('flowers', models.ManyToManyField(to='main_app.flower')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
