import requests


api_key = 'c9802cf912b771b5b06a1fb42cc83e39'

user_input = input('Enter City: ')
#print(user_input)

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod']=='404':
    print('No City found!')
else:
    #api health:
    #print(weather_data.status_code)
    #All weather data in json format
    #print(weather_data.json())

    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print(f'The weather in {user_input} is: {weather}')
    # To insert degree symbol use Alt and type 0176 on number pad 
    print(f'The tempurature in {user_input} is: {temp}°F')


