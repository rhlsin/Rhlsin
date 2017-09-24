import datetime
import forecastio
from forecastiopy import *
from geopy.geocoders import Nominatim

Lisbon=[]

api_key = 'a94a682750fdb4970407428c7795efaa'

def namcty(name):
    geolocator = Nominatim()
    location = geolocator.geocode(name)
    Lisbon.append(location.latitude)
    Lisbon.append(location.longitude)
    
def curtem():
    fio = ForecastIO.ForecastIO(api_key, latitude=Lisbon[0], longitude=Lisbon[1])

    current = FIOCurrently.FIOCurrently(fio)
    
    return current.temperature
def curpre():
    fio = ForecastIO.ForecastIO(api_key, latitude=Lisbon[0], longitude=Lisbon[1])

    current = FIOCurrently.FIOCurrently(fio)
    
    return current.pressure
def curhumi():
    fio = ForecastIO.ForecastIO(api_key, latitude=Lisbon[0], longitude=Lisbon[1])

    current = FIOCurrently.FIOCurrently(fio)
    
    return current.humidity
def curusm():
    fio = ForecastIO.ForecastIO(api_key, latitude=Lisbon[0], longitude=Lisbon[1])

    current = FIOCurrently.FIOCurrently(fio)
    
    return current.summary
def curpri():
    fio = ForecastIO.ForecastIO(api_key, latitude=Lisbon[0], longitude=Lisbon[1])

    current = FIOCurrently.FIOCurrently(fio)
    
    return current.precipProbability
def houtem(x,y,z):
    tem=[]
    time = datetime.datetime(x, y, z, 0, 0, 0)  #x=year,,y=mon,,z=date
    forecast = forecastio.load_forecast(api_key, Lisbon[0], Lisbon[1], time=time)

    by_hour = forecast.hourly()
    byHour = forecast.hourly()
    for hourlyData in byHour.data:
        tem.append(hourlyData.temperature)
    return tem
def houtim(x,y,z):
    tem=[]
    time = datetime.datetime(x, y, z, 0, 0, 0)
    forecast = forecastio.load_forecast(api_key, Lisbon[0], Lisbon[1], time=time)

    by_hour = forecast.hourly()
    byHour = forecast.hourly()
    for hourlyData in byHour.data:
        tem.append(hourlyData.time)
    return tem
def houpre(x,y,z):
    tem=[]
    time = datetime.datetime(x, y, z, 0, 0, 0)
    forecast = forecastio.load_forecast(api_key, Lisbon[0], Lisbon[1], time=time)
    by_hour = forecast.hourly()
    byHour = forecast.hourly()
    for hourlyData in byHour.data:
        tem.append(hourlyData.pressure)
    return tem

def houhumi(x,y,z):
    tem=[]
    time = datetime.datetime(x, y, z, 0, 0, 0)
    forecast = forecastio.load_forecast(api_key, Lisbon[0], Lisbon[1], time=time)
    by_hour = forecast.hourly()
    byHour = forecast.hourly()
    for hourlyData in byHour.data:
        tem.append(hourlyData.humidity)
    return tem
def housum(x,y,z):
    tem=[]
    time = datetime.datetime(x, y, z, 0, 0, 0)
    forecast = forecastio.load_forecast(api_key, Lisbon[0], Lisbon[1], time=time)
    by_hour = forecast.hourly()
    byHour = forecast.hourly()
    for hourlyData in byHour.data:
        tem.append(hourlyData.summary)
    return tem

def houpri(x,y,z):
    tem=[]
    time = datetime.datetime(x, y, z, 0, 0, 0)
    forecast = forecastio.load_forecast(api_key, Lisbon[0], Lisbon[1], time=time)
    by_hour = forecast.hourly()
    byHour = forecast.hourly()
    for hourlyData in byHour.data:
        tem.append(hourlyData.precipProbability)
    return tem
#namcty('bhimtal')
#x=houpre()
#print(x)
