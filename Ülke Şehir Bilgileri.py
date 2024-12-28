import requests

api_key = "84397657d6fa4a988e111b59a0b3ef0c"
ip_address = "88.238.60.184"

api_url = f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip_address}"

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    
    print(f"IP Adresi: {data['ip']}")
    print(f"Ülke: {data['country_name']}")
    print(f"Şehir: {data['city']}")
    print(f"Enlem: {data['latitude']}")
    print(f"Boylam: {data['longitude']}")
    print(f"Zaman Dilimi: {data['time_zone']['name']}")
else:
    print("API isteği başarısız oldu:", response.status_code)
