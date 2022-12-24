import telebot
import requests

bot = telebot.TeleBot('bot token')
OPEN_WEATHER_API_KEY = 'OpenWeatherMap token'
headers = {"X-Yandex-API-Key": "Yandex weather token"}

@bot.message_handler(content_types = ['text'])
def get_weather(message):
    city_name = message.text
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={OPEN_WEATHER_API_KEY}&units=metric"
    res = requests.get(url)
    coordinates_lon = res.json()['coord']['lon']
    coordinates_lat = res.json()['coord']['lat']
    url_2 = f'https://api.weather.yandex.ru/v2/informers?lat={coordinates_lat}&lon={coordinates_lon}'
    res_2 = requests.get(url=url_2, headers=headers)
    current_temp = res_2.json()['fact']['temp']
    bot.send_message(message.chat.id, f'Температура сейчас {current_temp}°C')

bot.polling(non_stop = True) 