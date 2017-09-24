import requests

def get_weather_forecast():
    # connecting to weather api
    url ="http://samples.openweathermap.org/data/2.5/weather?q=orlando&appid=b512318f5e1ca29297b1ae2a00d09895"
    weather_request = requests.get(url)
    weather_json = weather_request.json()
    print(weather_json)

    description = weather_json['weather'][0]['description']



    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']


    forecast = "The circus forecast for today is "
    forecast += description + ' with a highest temperature of ' + str(int(temp_max))
    forecast += ' and a lowest temperature of ' + str(int(temp_min))

    return forecast

