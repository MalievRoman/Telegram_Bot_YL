import requests
import json


with open("config.json") as file:
    data = json.load(file)


class Weather:
    def __init__(self, city):
        self.TOKEN = data["API_TOKEN"]
        try:
            request = requests.get(
                f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.TOKEN}&units=metric"
            )
            self.data = request.json()

        except Exception as ex:
            print(ex)
            print("Некорректное наименование города.")

    def temp(self):
        return f'Температура: {self.data["main"]["temp"]}°C, чувствуется как: {self.data["main"]["feels_like"]}°C.'

    def pressure(self):
        return f'Давление: {self.data["main"]["pressure"]} Па.'

    def humidity(self):
        return f'Влажность воздуха: {self.data["main"]["humidity"]}г/м³.'

    def all(self):
        return f'Температура: {self.data["main"]["temp"]}°C, чувствуется как: {self.data["main"]["feels_like"]}°C. \n' \
               f'Давление: {self.data["main"]["pressure"]} Па.\n' \
               f'Влажность воздуха: {self.data["main"]["humidity"]}г/м³.\n'\
               f'В корне проекта появился файл с сохраненными данными'