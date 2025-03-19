import random
import datetime

# Struktur Data: List film dalam bentuk dictionary
film = [
    {"id": 1, "judul": "Interstellar", "genre": "Sci-Fi", "tiket": 5},
    {"id": 2, "judul": "Inception", "genre": "Action", "tiket": 3},
    {"id": 3, "judul": "The Dark Knight", "genre": "Action", "tiket": 4},
]

# Fungsi untuk menampilkan daftar film
def tampilkan_film():
    print("\nDaftar Film yang Tersedia:")
    for f in film:
        print(f"{f['id']}. {f['judul']} - {f['genre']} (Tiket tersedia: {f['tiket']})")

# Fungsi untuk memesan tiket film
def pesan_tiket():
    tampilkan_film()
    try:
        id_film = int(input("\nMasukkan ID film yang ingin ditonton: "))
        for f in film:
            if f["id"] == id_film:
                if f["tiket"] > 0:
                    f["tiket"] -= 1
                    jam_tayang = datetime.datetime.now() + datetime.timedelta(minutes=random.randint(30, 120))
                    print(f"\nTiket untuk '{f['judul']}' berhasil dipesan!")
                    print(f"Jam tayang: {jam_tayang.strftime('%H:%M:%S')}")
                    input("\nTekan Enter untuk melanjutkan...")  # Solusi agar tidak langsung keluar
                    return
                else:
                    print("\nMaaf, tiket sudah habis!")
                    input("\nTekan Enter untuk melanjutkan...")
                    return
        print("\nID film tidak ditemukan!")
    except ValueError:
        print("\nMasukkan ID film yang valid!")
    input("\nTekan Enter untuk melanjutkan...")  # Supaya tidak langsung keluar

# Program utama
while True:
    print("\n=== Sistem Pemesanan Tiket Film ===")
    print("1. Lihat Daftar Film")
    print("2. Pesan Tiket")
    print("3. Keluar")
    
    pilihan = input("Pilih menu (1/2/3): ")
    
    if pilihan == "1":
        tampilkan_film()
        input("\nTekan Enter untuk melanjutkan...")
    elif pilihan == "2":
        pesan_tiket()
    elif pilihan == "3":
        print("\nTerima kasih telah menggunakan sistem pemesanan tiket!")
        break
    else:
        print("\nPilihan tidak valid, coba lagi!")
        input("\nTekan Enter untuk melanjutkan...")
