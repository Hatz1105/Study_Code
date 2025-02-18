import socket
import threading
from queue import Queue

# Target yang mau discan (ganti sesuai kebutuhan)
TARGET = "scanme.nmap.org"  # Bisa pakai IP atau domain
PORTS = range(1, 1025)  # Port yang akan discan (1-1024)
THREADS = 50  # Jumlah thread (biar lebih cepat)
OUTPUT_FILE = "port_scan_results.txt"  # File untuk simpan hasil scan

# Queue untuk menyimpan port yang akan diproses
queue = Queue()

# Fungsi untuk scan satu port
def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout biar gak nunggu lama
        result = sock.connect_ex((target, port))  # Coba koneksi ke port
        
        if result == 0:  # Port terbuka
            try:
                service = socket.getservbyport(port)  # Cek service yang jalan
            except:
                service = "Unknown"
            print(f"[+] Port {port} OPEN ({service})")
            save_to_file(f"[+] Port {port} OPEN ({service})")
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

# Fungsi untuk menyimpan hasil scan ke file
def save_to_file(data):
    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
        f.write(data + "\n")

# Fungsi worker untuk multi-threading
def worker():
    while not queue.empty():
        port = queue.get()
        scan_port(TARGET, port)
        queue.task_done()

# Masukkan port ke dalam queue
for port in PORTS:
    queue.put(port)

# Buat threads untuk scan lebih cepat
threads = []
for _ in range(THREADS):
    thread = threading.Thread(target=worker)
    thread.start()
    threads.append(thread)

# Tunggu semua thread selesai
for thread in threads:
    thread.join()

print(f"✅ Scan selesai! Hasil disimpan di {OUTPUT_FILE}")
