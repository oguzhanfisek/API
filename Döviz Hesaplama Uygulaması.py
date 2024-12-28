import requests

def get_exchange_rate(base_currency, target_currency, api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if target_currency in data['conversion_rates']:
            return data['conversion_rates'][target_currency]
        else:
            print(f"{target_currency} için döviz kuru bulunamadı.")
            return None
    else:
        print("API isteği başarısız oldu.")
        return None

def convert_currency(amount, base_currency, target_currency, api_key):
    rate = get_exchange_rate(base_currency, target_currency, api_key)
    
    if rate:
        converted_amount = amount * rate
        print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
    else:
        print("Döviz kuru hesaplanamadı.")

base_currency = input("Base Currency (örn: USD): ").upper()
target_currency = input("Target Currency (örn: EUR): ").upper()
amount = float(input("Amount to Convert: "))
api_key = "b159bcf6b4b067c7fc2a4962"

convert_currency(amount, base_currency, target_currency, api_key)
