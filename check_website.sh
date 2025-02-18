#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <website>"
    exit 1
fi

echo "🔎 Mengecek status website: $1 ..."

# Cek koneksi dengan ping (3 kali)
ping -c 3 "$1" > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✅ $1 dapat di-ping!"
else
    echo "⚠️ $1 tidak merespon ping (mungkin diblokir)."
fi

# Cek status HTTP dengan curl, fallback ke wget kalau curl gagal
if command -v curl &> /dev/null; then
    http_status=$(curl -o /dev/null -s -w "%{http_code}" "http://$1")
    https_status=$(curl -o /dev/null -s -w "%{http_code}" "https://$1")
elif command -v wget &> /dev/null; then
    http_status=$(wget --server-response --spider "http://$1" 2>&1 | awk '/HTTP/{print $2}' | head -n 1)
    https_status=$(wget --server-response --spider "https://$1" 2>&1 | awk '/HTTP/{print $2}' | head -n 1)
else
    echo "❌ Tidak ada curl atau wget! Install salah satu dulu."
    exit 1
fi

if [ "$http_status" -eq 200 ] || [ "$https_status" -eq 200 ]; then
    echo "✅ Website aktif!"
elif [ "$http_status" -eq 301 ]; then
    echo "🔄 Redirect ke HTTPS (kode 301)."
    if [ "$https_status" -eq 200 ]; then
        echo "✅ HTTPS aktif!"
    else
        echo "❌ HTTPS juga tidak bisa diakses."
    fi
else
    echo "❌ Website memberikan kode HTTP: $http_status / $https_status"
fi

