import requests

url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Harga Ethereum : ${data['ethereum']['usd']}")
else:
    print("Gagal Mengambil Harga Ethereum.")