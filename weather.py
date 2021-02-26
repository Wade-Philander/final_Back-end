from flask import Flask
import requests
import sqlite3

weather = Flask(__name__)

@weather.route('/',methods=['GET'])
def get_weather_today():

    api_url ="http://api.openweathermap.org/data/2.5/forecast?q=London&appid=e30a3785da67bd9d83b65bf8933359b5"

    response= requests.get(api_url)
    json_data=response.json()

    
    main_weather = json_data ['list'][2]['weather'][0]['main']
    describe_weather = json_data ['list'][2]['weather'][0]['description']
    min_weather = json_data ['list'][0]['main']['temp_min']
    max_weather = json_data ['list'][0]['main']['temp_max']

    weather_data = str(main_weather)+" "+str(describe_weather) +" "+ str(min_weather) +" "+ str(max_weather)
    
    print(weather_data)

    return weather_data

if __name__ =="__main__":
    weather.run()
