import requests
import json
import datetime

TOKEN = '089538441dfd5eebba20e7fee5df20a2'
BASE_URL = 'https://api.openweathermap.org/data/2.5/forecast/daily?q='


def temp_in_celsius(temperature):
    return str(round(temperature - 273))


def parse_response(resp, date):
    weather_list = resp['list']

    for day in weather_list:
        not_format_date = datetime.date.fromtimestamp(int(day['dt']))
        if date == not_format_date.strftime('%d-%m-%Y'):
            print(f'Weather in {resp["city"]["name"]} {resp["city"]["country"]} is: ')
            print(f'Temperature: {temp_in_celsius(day["temp"]["day"])} C')
            print(f'Feels like: {temp_in_celsius(day["feels_like"]["day"])} C')
            print(f'Min temperature: {temp_in_celsius(day["temp"]["min"])} C')
            print(f'Max temperature: {temp_in_celsius(day["temp"]["max"])} C')
            print('Pressure: ' + str(day['pressure']) + ' hPa')
            print('Humidity: ' + str(day['humidity']) + ' %')
            break


def get_weather(day=None, city='Kyiv'):
    url = BASE_URL + f'{city}&cnt=16&appid={TOKEN}'
    response = requests.get(url)
    if response.status_code != 200:
        print('City not found')
    else:
        text_response = json.loads(response.text)
        if not day:
            int_date = int(text_response['list'][0]['dt'])
            day = datetime.date.fromtimestamp(int_date).strftime('%d-%m-%Y')
        parse_response(text_response, day)


# TODO parse days


if __name__ == '__main__':
    get_weather()
    town = None
    while True:
        town = input('\nEnter name of city or type "exit" to exit program \n')
        date = input('Enter the date in format "dd-mm-yyyy". Date must be no '
                     'later than 16 days from today\n')
        if town == 'exit':
            break
        get_weather(date, town)
