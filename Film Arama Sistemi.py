import requests

api_key = "29b67432"
base_url = "http://www.omdbapi.com/"

def search_movie(movie_name):
    params = {
        't': movie_name,
        'apikey': api_key  
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
        if data['Response'] == 'True':
            print(f"Film: {data['Title']}")
            print(f"Yıl: {data['Year']}")
            print(f"Tür: {data['Genre']}")
            print(f"Yönetmen: {data['Director']}")
            print(f"Özet: {data['Plot']}")
            print(f"IMDB Puanı: {data['imdbRating']}")
        else:
            print("Film bulunamadı!")
    else:
        print("API isteği başarısız oldu. Lütfen tekrar deneyin.")

movie_name = input("Aramak istediğiniz filmi girin: ")

search_movie(movie_name)
