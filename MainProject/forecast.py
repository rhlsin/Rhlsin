import datetime
import forecastio
from forecastiopy import *
from geopy.geocoders import Nominatim


def forecaste(city):
        temp=[]
        time=[]
        geolocator = Nominatim()
        #print("enter city name")
        #city=input()
        location = geolocator.geocode(city)
        api_key = 'a94a682750fdb4970407428c7795efaa'
        Lisbon = [location.latitude,location.longitude]
        lat = location.latitude
        lng = location.longitude
        #8 days ahead
        time = datetime.datetime(2017, 4, 23, 0, 0, 0)
        fio = ForecastIO.ForecastIO(api_key, latitude=Lisbon[0], longitude=Lisbon[1])
        forecast = forecastio.load_forecast(api_key, lat, lng, time=time)
        current = FIOCurrently.FIOCurrently(fio)
        #print ("===========Currently Data=========")
        #print('Temperature:', current.humidity)

        #print ("===========Currently Data=========")
        #print (forecast.currently())

        #print ("===========Hourly Data=========")
        by_hour = forecast.hourly()
        byHour = forecast.hourly()
        for hourlyData in byHour.data:
                temp.append(hourlyData.temperature)
                time.append(hourlyData.time)
        #for hourlyData in byHour.data:
         #       print ("temp=",hourlyData.temperature,"time",hourlyData.time)
        #temperature,pressure,humidity,summary,precipProbability,icon,precipitation
        #print ("===========Daily Data=========")
        by_day = forecast.daily()
        #print ("Daily Summary: %s" % (by_day.summary))

        #for daily_data_point in by_day.data:
            #print (daily_data_point)
        return temp,time
       

#q=forecaste('bhimtal')
#print(q)
