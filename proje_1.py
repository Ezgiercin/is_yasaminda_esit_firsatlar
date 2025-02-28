import requests

API_KEY = "c99c0680cb5043b7e33db075ed3ebc04"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# Hava durumunu çekme fonksiyonu
def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "tr"
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data

weather_list = []

# CREATE - Yeni hava durumu verisi ekleme
def create_weather(data):
    weather_list.append(data)
    return "Hava durumu verisi başarıyla eklendi!"


# SHOW - Hava durumu verilerini gösterme
def show_weather():
    return weather_list


# UPDATE - Hava durumu verisini güncelleme
def update_weather(index, updated_data):
    if 0 <= index < len(weather_list):
        weather_list[index] = updated_data
        return "Hava durumu verisi başarıyla güncellendi!"
    return "Geçersiz indeks."


# DELETE - Hava durumu verisini silme
def delete_weather(index):
    if 0 <= index < len(weather_list):
        del weather_list[index]
        return "Hava durumu verisi başarıyla silindi!"
    return "Geçersiz indeks."


#test example for Istanbul

weather = get_weather("Istanbul")
print(weather)
