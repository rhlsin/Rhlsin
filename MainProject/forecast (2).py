import input
import datetime
import forecastio
from forecastiopy import *
from geopy.geocoders import Nominatim

def get_weather():
        geolocator = Nominatim()
        location = geolocator.geocode(input.city)
        api_key = 'a94a682750fdb4970407428c7795efaa'
        Lisbon = [location.latitude,location.longitude]

        #8 days ahead
        d = degree_sign= u'\N{DEGREE SIGN}'
        time = datetime.datetime(2017, 4, 18, 0, 0, 0)
        fio = ForecastIO.ForecastIO(api_key, latitude=Lisbon[0], longitude=Lisbon[1])
        forecast = forecastio.load_forecast(api_key, Lisbon[0], Lisbon[1], time=time)
        current = FIOCurrently.FIOCurrently(fio)
##        print ("===========Current Data=========")
##        print("Temperature : ", str(int(current.temperature)) +d+ "C")
##        print("Pressure : ", current.pressure )
##        print("Humidity : ", current.humidity)
##        print("Summary : ", current.summary)
##        print("Precipitation = ",current.precipProbability)
##
##        print("===========Hourly Data=========")
        byHour = forecast.hourly()
##        for hourlyData in byHour.data:
##                print ("Temperature:", str(int(hourlyData.temperature))+d+"C","Pressure :",hourlyData.pressure, "Precipitation:" \
##                       , hourlyData.precipProbability, "Humidity:", hourlyData.humidity, "Summary:",hourlyData.summary)



def main():
    get_weather()


main()
