from .models import Weather, Location, Temperature

from django.db import models


from rest_framework import serializers
from django.core.validators import *
from django.core import checks, exceptions, validators

# class LocationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Location
#         fields = ['lat','lon','city','state']
#
#     def create(self, validated_data):
#         return Location.objects.create(**validated_data)
#
# class WeatherSerailzer(serializers.ModelSerializer):
#     location = LocationSerializer(many=False)
#
#     class Meta:
#         model = Weather
#         # fields = ['id','date','location','temperature']
#         fields = '__all__'
#
#     def create(self, validated_data):
#         location_data = validated_data.pop('location')
#         print (location_data)
#         l = Location.objects.create(**location_data)
#         print (l)
#         w = Weather.objects.create(location= l, **validated_data)
#         print (w)
#         return w


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('lat','lon','city','state')

    def create(self, validated_data):
        return Location.objects.create(**validated_data)

class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ('temperature',)


class WeatherSerializer(serializers.ModelSerializer):
    temperature = TemperatureSerializer(many=True)
    location = LocationSerializer(many=False)

    class Meta:
        model = Weather
        fields = ('id','date','location','temperature')

    def create(self, validated_data):
        # print (validated_data['location'])
        location_data = validated_data.pop('location')
        # print("location_data\r\n")
        # print(location_data)
        temp_datas = validated_data.pop('temperature')
        # print("temps_data\r\n")
        # print(temp_datas)
        w = Weather.objects.create(**validated_data)
        l = Location.objects.create(weather=w, **location_data)
        for temp_data in temp_datas:
            Temperature.objects.create(weather=w,**temp_data)
        return w

    def to_representation(self, instance):
        """Convert `username` to lowercase."""
        # print ("super chal ra")
        ret = super().to_representation(instance)
        # print (ret)
        # print (ret['temperature'])

        temp_list = []
        for temps in ret['temperature']:
            # print (temps)
            # print(list(temps.items()))
            #
            # print ("item\r\n")
            # print(list(temps.items())[0][1])
            temp_list.append(list(temps.items())[0][1])
        # print (ret)

        # print(temp_list)
        ret['temperature'] = temp_list
        return ret

    def to_internal_value(self, data):
        # print ("chal ra")
        # print (data.get('temperature'))

        from collections import OrderedDict
        l_o_od = []
        for i in data.get('temperature'):
            # print (i)
            my_dictionary = OrderedDict()
            my_dictionary['temperature'] = i
            l_o_od.append(my_dictionary)

        # print (l_o_od)
        data['temperature'] = l_o_od
        # print ("chal ra2")
        # print (data.get('temperature'))
        ret = super().to_internal_value(data)
        return ret
