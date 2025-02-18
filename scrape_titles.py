import requests
from bs4 import BeautifulSoup

url = "https://coinmarketcap.com"  # Ganti dengan website target
headers = {"User-Agent": "Mozilla/5.0"}  # Biar gak terblokir

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find_all("h1")  # Ambil semua <h1>
    for title in titles:
        print(title.text.strip())
else:
    print(f"Gagal mengambil data. Status code: {response.status_code}")
