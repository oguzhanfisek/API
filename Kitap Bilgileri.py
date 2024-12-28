import requests

api_url = "https://www.googleapis.com/books/v1/volumes"

search_query = "Harry Potter" 

# API'ye istek gönderme
response = requests.get(api_url, params={"q": search_query})

if response.status_code == 200:
    data = response.json()  
    
    if "items" in data:
        for i, item in enumerate(data["items"][:3]):
            title = item["volumeInfo"].get("title", "Başlık Bulunamadı")
            authors = item["volumeInfo"].get("authors", ["Yazar Bulunamadı"])
            published_date = item["volumeInfo"].get("publishedDate", "Yayın Tarihi Bulunamadı")
            description = item["volumeInfo"].get("description", "Açıklama Bulunamadı")
            print(f"\nKitap {i + 1}:")
            print(f"Başlık: {title}")
            print(f"Yazar(lar): {', '.join(authors)}")
            print(f"Yayın Tarihi: {published_date}")
            print(f"Açıklama: {description[:200]}...")  
    else:
        print("Kitap bulunamadı.")
else:
    print("API isteği başarısız oldu:", response.status_code)
