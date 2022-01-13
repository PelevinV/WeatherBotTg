import requests
import datetime
from pprint import pprint
from config import open_weather_token


def get_weather(city, open_weather_token):
    code_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U0001F327",
        "Drizzle": "Изморось \U0001F327",
        "Thunderstorm": "Гроза \U0001F329",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B",
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric")
        data = r.json()
        pprint(data)

        weather_description = data["weather"][0]["main"]
        if weather_description in code_smile:
            wd = code_smile[weather_description]
        else:
            wd = "Не пойму, какая на улице погода. Посмотри сам)"

        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        print(f"Город: {city}\nТемпература: {cur_weather}°C {wd}\nВлажность: {humidity}\n"
              f"Давление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
              f"Восход: {sunrise_timestamp}\nЗакат: {sunset_timestamp}\n"
              f"Продуктивного дня!")

    except Exception as ex:
        print(ex)
        print("Проверьте название города")


def main():
    city = input("Введите город: ")
    get_weather(city, open_weather_token)


if __name__ == "__main__":
    main()
