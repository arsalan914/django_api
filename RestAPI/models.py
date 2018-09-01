# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django import forms
from django.contrib.postgres.fields import ArrayField
from django.core.validators import *
from django.core import checks, exceptions, validators


class Weather(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField()

    def __str__(self):
        return str(self.date) + " " + str(self.id)

class Location(models.Model):
    lat = models.FloatField(default=0)
    lon = models.FloatField(default=0)
    city = models.CharField(max_length=300)
    state = models.CharField(max_length=300)
    weather = models.OneToOneField(Weather,related_name='location', on_delete=models.CASCADE)

    def __str__(self):
        return (self.city) + " " + (self.state) + " "  + str(self.lat) + " " + str(self.lon) + " " + str(self.weather_id)


class Temperature(models.Model):
    temperature = models.FloatField(default=0)
    weather = models.ForeignKey(Weather,related_name='temperature', on_delete=models.CASCADE)

