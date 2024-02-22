import requests
import os
from dotenv import load_dotenv

def getWeather(city, apiKey):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang=ja&units=metric'
    response = requests.get(url)

    if response.status_code != 200:
        return f'天気の取得に失敗しました。有効な都市名を再入力してください。 {response.status_code}'
    
    data = response.json()
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    return f"- {city}の現在の天気: {description}、気温: {temp}°C"

def main():
    while True:
        print("都市の名前を入力してください 終了するにはqを押してください")
        print("例: Tokyo,JP / London,GB / NewYork,US")

        city = input('>')

        load_dotenv('../.env')
        apiKey = os.environ.get('ApiKey')

        if city == 'q':
            break

        data = getWeather(city, apiKey)
        print('--------')
        print(data)

if __name__ == '__main__':
    main()
