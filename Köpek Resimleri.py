import requests
import json

api_url = "https://dog.ceo/api/breeds/image/random"

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    dog_image_url = data['message'] 
    print("Rastgele Köpek Fotoğrafı URL'si:", dog_image_url)
else:
    print("API isteği başarısız oldu:", response.status_code)
