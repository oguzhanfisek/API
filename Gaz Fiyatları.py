import requests
import json

api_url = "https://api.collectapi.com"
headers = {
    'X-Api-Key': '4tLlQnT2lVWAB8aUqCZKg6:7BBWYRqADwzfcS5O4zyaLO'  # Burada 'YOUR_API_KEY' kısmını kendi API anahtarınızla değiştirin.
}

state = input("Gaz fiyatlarını öğrenmek istediğiniz eyaletin kısaltmasını girin (örneğin, CA, NY): ")

response = requests.get(f"{api_url}?state={state}", headers=headers)

if response.status_code == 200:
    data = response.json()
    if data:
        print(f"{state} eyaletindeki gaz fiyatları:")
        for item in data:
            print(f"  {item['station_name']}: {item['price']} USD")
    else:
        print("Bu eyalette gaz fiyatları bulunamadı.")
else:
    print("API isteği başarısız oldu:", response.status_code)
