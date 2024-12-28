import requests

url = 'https://www.trendyol.com/'

response = requests.get(url)

if response.status_code == 200:
    html_data = response.text
    print("Web sayfasının içeriği:")
    print(html_data)
else:
    print(f"İstek başarısız oldu. Durum Kodu: {response.status_code}")
