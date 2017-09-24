import input
import datetime
import forecastio
from forecastiopy import *
from geopy.geocoders import Nominatim


def get_weather_forecast():
        lst = []
        geolocator = Nominatim()
        #change name of city
        location = geolocator.geocode(input.city)
        api_key = 'a94a682750fdb4970407428c7795efaa'
        Lisbon = [location.latitude,location.longitude]

        #8 days ahead
        #d = degree_sign= u'\N{DEGREE SIGN}'
        time = datetime.datetime(2017, 4, 18, 0, 0, 0)
        fio = ForecastIO.ForecastIO(api_key, latitude=Lisbon[0], longitude=Lisbon[1])
        forecast = forecastio.load_forecast(api_key, Lisbon[0], Lisbon[1], time=time)
        current = FIOCurrently.FIOCurrently(fio)
        t = str(int(current.temperature))
        lst.append(t)
        ps = str(current.pressure)
        lst.append(ps)
        h = str(current.humidity)
        lst.append(h)
        s = current.summary
        lst.append(s)
        ppt = str(current.precipProbability)
        lst.append(ppt)

        forecast = "Temperature  : " +lst[0]+' degree celsius '+'\n'
        forecast += "Atmoshpheric Pressure  : " + lst[1] + 'hpa'+'\n'
        forecast += "Humidity  : " +lst[2] +'\n'
        forecast += "Precipitation Probability  : " +lst[4] +'\n'
        forecast += "Weather Summary  : "+lst[3]

        return forecast




get_weather_forecast()
