import requests

api_key = "8abe0ad65477dcff285db7aa31e509d7"
base_url = "https://api.openweathermap.org/data/2.5/weather?"

city_name = input("Şehir adını girin: ")

response = requests.get(base_url, params={
    "q": city_name,
    "appid": api_key,
    "units": "metric", 
    "lang": "tr"  
})

if response.status_code == 200:
    data = response.json()
    
    city = data["name"]
    
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    print(f"Şehir: {city}")
    print(f"Sıcaklık: {temperature}°C")
    print(f"Açıklama: {description}")
    print(f"Nem: {humidity}%")
    print(f"Rüzgar Hızı: {wind_speed} m/s")

else:
    print("Hava durumu bilgisi alınırken bir hata oluştu. Lütfen şehir adını kontrol edin.")
    