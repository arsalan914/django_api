from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import WeatherSerializer
from django.db.models.functions import Lower


class StockList(APIView):
    def get(self,request):
        try :
            if len(request.GET) == 0 and Weather.objects.all().count() != 0:
                # print (Weather.objects.all()[0])
                s = WeatherSerializer(Weather.objects.all(), many=True)
                # print (s)

                return Response(s.data, status=200)

            elif len(request.GET) == 2:
                lat = self.request.GET.get('lat')
                lon = self.request.GET.get('lon')

                if lat != None and lat != "" and \
                   lon != None and lon != "":

                    # print(Location.objects.filter(lat=lat, lon=lon).select_related('weather__location').values('weather__id'))
                    #print(Weather.objects.filter(id__in=Location.objects.filter(lat=lat, lon=lon).select_related('weather__location').values('weather__id')))
                    # values('first_name')
                    # print (Weather.objects.all())
                    # print (Location.objects.all())

                    if Weather.objects.filter(id__in=Location.objects.filter(lat=lat, lon=lon).select_related('weather__location').values('weather__id')).count() != 0:
                        s = WeatherSerializer(Weather.objects.filter(id__in=Location.objects.filter(lat=lat, lon=lon).select_related('weather__location').values('weather__id')), many=True)

                        return Response(s.data, status=200)
        except:
            pass

        return Response(status=404)

    def post(self, request):
        # return "test post"
        serializer = WeatherSerializer(data=request.data)
        # print (serializer)
        if serializer.is_valid():
            # print ('valid')
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=400)

    def delete(self,request):
        start = self.request.GET.get('start')
        end = self.request.GET.get('end')
        lat = self.request.GET.get('lat')
        lon = self.request.GET.get('lon')

        deleted = 0

        if start != None and start != "" and \
           end != None and end != "" and \
           lat != None and lat != "" and \
           lon != None and lon != "" :
            all_w_in_date = Weather.objects.filter(date__range=[start, end])
            print (all_w_in_date)
            for w in all_w_in_date:
                try:
                    Location.objects.get(weather=w, lat=lat, lon=lon)
                    w.delete()
                    deleted = 1
                except Location.DoesNotExist:
                    pass


        elif len(request.GET) ==  0:
            all_w = Weather.objects.all()
            for w in all_w:
                deleted = 1
                w.delete()

        if (deleted == 1):
            return Response(status=200)
        else:
            return Response(status=404)

class StockList2(APIView):
    def get(self,request):

        start = self.request.GET.get('start')
        end = self.request.GET.get('end')

        deleted = 0

        if start != None and start != "" and \
           end != None and end != "":

            # print (Location.objects.all().select_related('weather__location'))
            all_locations = Location.objects.all().order_by(Lower('city'), Lower('state'))

            import json

            #set city with data
            all_data = []
            data_cities = []
            for loc in all_locations:

                all_w_in_date = Weather.objects.filter(date__range=[start, end])

                found = 0

                for w in all_w_in_date:

                    if w.id == loc.weather_id:

                        data_cities.append(loc.city)
                        # print ("found weather info")
                        # print (str(loc.id))
                        # print ("\r\ncity=")
                        # print (loc.city)

                        found = 1

                        temps = (Temperature.objects.filter(weather=w))
                        min =10000
                        max =0

                        for t in temps:
                            if t.temperature < min:
                                min = t.temperature
                            if t.temperature > max:
                                max = t.temperature
                        # print ("\r\n min=")
                        # print (str(min))
                        # print ("\r\n max")
                        # print (str(max))

                        data1 = {}
                        data1['lat'] = loc.lat
                        data1['lon'] = loc.lon
                        data1['city'] = loc.city
                        data1['state'] = loc.state
                        data1['highest'] = max
                        data1['lowest'] = min

                        all_data.append(data1)

                if found == 0 and loc.city not in data_cities:
                    # print("not found weather info " )
                    # print(str(loc.city))
                    data1 = {}
                    data1['lat'] = loc.lat
                    data1['lon'] = loc.lon
                    data1['city'] = loc.city
                    data1['state'] = loc.state
                    data1['message'] = "There is no weather data in the given date range"

                    all_data.append(data1)

                    # locations = (Location.objects.get(weather=w))

            #set city without data
            # for loc in all_locations:
            #
            #     if loc.city not in data_cities:
            #
            #         data1 = {}
            #         data1['lat'] = loc.lat
            #         data1['lon'] = loc.lon
            #         data1['city'] = loc.city
            #         data1['state'] = loc.state
            #         data1['message'] = "smb"
            #
            #         all_data.append(data1)

            data2 = {}
            data2['data'] = all_data


            #set min max
            city = ""
            for d in all_data:
                city = d['city']


                if city in data_cities:
                    min = d['lowest']
                    max = d['highest']

                    for dd in all_data:
                        if city == dd['city']:
                            if dd['lowest'] < min:
                                min = dd['lowest']
                            if dd['highest'] > max:
                                max = dd['highest']

                    d['lowest'] = min
                    d['highest'] = max

            #remove duplicates
            all_data2 = []
            for d in all_data:
                found = 0
                for d2 in all_data2:
                    if d['city'] == d2['city']:
                        found = 1
                if found == 0:
                    all_data2.append(d)

            # json_data = json.dumps(data2, indent = 4)
            # print (json_data)

        return Response(all_data2, status=200)
