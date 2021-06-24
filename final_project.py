
import requests
from datetime import datetime

api_key = 'a4432bde89065401a05dc13ee4de07f7'
#by using os module the important api key is hidden

location = input("enter your current location ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

if api_data['cod'] == '404':
    print('INVALID city: {},please check your city name'.format(location))
else:
    Temperature = ((api_data['main']['temp']) - 273.15)
    Weather_desc = (api_data['weather'][0]['description'])
    Humidity = (api_data['main']['humidity'])
    Wind_speed = (api_data['wind']['speed'])
    Date_time = datetime.now().strftime("%d %b %y | %I:%M:%S %p")


print("   ********************************************************")
print("   >  weather report for {} on {}  <".format(location.upper(), Date_time))
print("   ********************************************************")

print("   -->current temperature : {:.2F} Deg c".format(Temperature))
print("   -->weather description :", Weather_desc)
print("   -->current humidity    :", Humidity, '%')
print("   -->current wind speed  :", Wind_speed, 'kmph')











