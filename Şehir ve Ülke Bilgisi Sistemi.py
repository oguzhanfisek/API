import requests

base_url = "https://restcountries.com/v3.1/name/"

def get_country_info(country_name):
    response = requests.get(f"{base_url}{country_name}")
    
    if response.status_code == 200:
        data = response.json()  
        
        country = data[0]  
        name = country["name"]["common"]  
        capital = country.get("capital", ["Bilgi yok"])[0]  
        region = country["region"]  
        subregion = country["subregion"]  
        languages = ", ".join(country["languages"].values()) if "languages" in country else "Bilgi yok" 
        currencies = ", ".join(currency["name"] for currency in country.get("currencies", {}).values()) if "currencies" in country else "Bilgi yok" 
        
        print(f"Ülke: {name}")
        print(f"Başkent: {capital}")
        print(f"Bölge: {region}")
        print(f"Alt Bölge: {subregion}")
        print(f"Diller: {languages}")
        print(f"Para Birimleri: {currencies}")
    else:
        print(f"{country_name} hakkında bilgi alınamadı. Lütfen geçerli bir ülke adı girin.")

country_name = input("Bilgi almak istediğiniz ülkeyi girin: ")

get_country_info(country_name)
