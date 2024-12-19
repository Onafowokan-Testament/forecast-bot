import telebot
import requests
from flask import Flask
BOT_API_KEY = 'api_key'
bot = telebot.TeleBot(BOT_API_KEY)

app= Flask(__name__)


import requests
import os
API_KEY ="api_key"
account_sid = "account_sid"
auth_token = "auth_token"


@app.route('/')
    @bot.message_handler(commands=['weather_forecast', 'weather'])
    def check_weather_forecast(message):
    
        parameter ={"lat" :lat,
                    "lon" :lon,
                    "appid" : API_KEY,
                    "exclude": "current,minutely,daily"
        }
        response =requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameter)

        weather_data = response.json()
        print(weather_data)
        weather_slice= weather_data["hourly"][:12]
        will_rain = False
        for hour_data in weather_slice:
            weather_id = hour_data["weather"][0]["id"]
            if weather_id <900:
                will_rain = True
        if will_rain:
            print('True weather')
            bot.send_message(message.chat.id, " It is  going  rain today")
            
        else:
            print('False')
            bot.send_message(message.chat.id,"It will not rain today")
    bot.polling()

if __name__ == "__main__":
    app.run()
