import speedtest
import time
from datetime import datetime

# Fungsi untuk menjalankan speed test
def run_speed_test():
    st = speedtest.Speedtest()
    st.get_best_server()  # Pilih server terbaik
    
    # Ambil info server
    server = st.best
    server_name = server['name']
    server_country = server['country']
    provider = server['sponsor']

    # Jalankan speed test
    ping = st.results.ping
    download_speed = st.download() / 1_000_000  # Konversi ke Mbps
    upload_speed = st.upload() / 1_000_000  # Konversi ke Mbps

    # Format hasil dengan 2 desimal
    result = (
        f"\n📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"🌍 Server: {server_name}, {server_country} (Provider: {provider})\n"
        f"📍 Ping: {ping:.2f} ms\n"
        f"📡 Download: {download_speed:.2f} Mbps\n"
        f"🚀 Upload: {upload_speed:.2f} Mbps\n"
        "---------------------------"
    )
    
    print(result)  # Tampilkan hasil di terminal
    save_to_log(result)  # Simpan ke log file

# Fungsi untuk menyimpan hasil ke file dengan encoding UTF-8
def save_to_log(data, filename="speedtest_log.txt"):
    with open(filename, "a", encoding="utf-8") as file:  # Fix encoding error
        file.write(data + "\n")

# Loop otomatis setiap X detik (misal: 60 detik)
INTERVAL = 60  # Ubah sesuai kebutuhan
while True:
    run_speed_test()
    print(f"⏳ Menunggu {INTERVAL} detik sebelum tes berikutnya...\n")
    time.sleep(INTERVAL)
