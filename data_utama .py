import csv
from collections import deque

# File database
DB_FILE = "tiket_bioskop.csv"

# Data film (Hash Map)
film_data = {
    1: {"judul": "Qodrat", "jam": "14:00"},
    2: {"judul": "Tumbal proyek", "jam": "17:00"},
    3: {"judul": "Toy", "jam": "20:00"}
}

# Queue untuk antrian pembelian
antrian = deque()

# ===== Fungsi CRUD =====
def load_data():
    data = []
    try:
        with open(DB_FILE, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            data = list(reader)
    except FileNotFoundError:
        pass
    return data

def save_data(data):
    with open(DB_FILE, mode="w", newline="") as file:
        fieldnames = ["id", "nama", "film", "jam", "jumlah"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def create_ticket():
    data = load_data()
    id_tiket = str(len(data) + 1)
    nama = input("Masukkan nama pembeli: ")
    print("Pilih film:")
    for k, v in film_data.items():
        print(f"{k}. {v['judul']} ({v['jam']})")
    pilihan = int(input("Nomor film: "))
    jumlah = input("Jumlah tiket: ")

    tiket = {
        "id": id_tiket,
        "nama": nama,
        "film": film_data[pilihan]["judul"],
        "jam": film_data[pilihan]["jam"],
        "jumlah": jumlah
    }
    data.append(tiket)
    save_data(data)
    antrian.append(nama)
    print("✅ Tiket berhasil dipesan!")

def read_tickets():
    data = load_data()
    if not data:
        print("Belum ada data tiket.")
    else:
        for d in data:
            print(d)

def update_ticket():
    data = load_data()
    id_tiket = input("Masukkan ID tiket yang ingin diubah: ")
    for d in data:
        if d["id"] == id_tiket:
            d["nama"] = input("Nama baru: ")
            d["jumlah"] = input("Jumlah tiket baru: ")
            save_data(data)
            print("✅ Tiket berhasil diupdate!")
            return
    print("❌ Tiket tidak ditemukan.")

def delete_ticket():
    data = load_data()
    id_tiket = input("Masukkan ID tiket yang ingin dihapus: ")
    new_data = [d for d in data if d["id"] != id_tiket]
    save_data(new_data)
    print("✅ Tiket berhasil dihapus!")

# ===== Sorting & Searching =====
def search_ticket():
    data = load_data()
    nama = input("Cari tiket berdasarkan nama: ")
    hasil = [d for d in data if d["nama"].lower() == nama.lower()]
    if hasil:
        for h in hasil:
            print(h)
    else:
        print("❌ Tiket tidak ditemukan.")

def sort_tickets():
    data = load_data()
    sorted_data = sorted(data, key=lambda x: x["jam"])
    for d in sorted_data:
        print(d)

# ===== Menu Utama =====
def menu():
    while True:
        print("\n=== Sistem Pemesanan Tiket Bioskop ===")
        print("1. Pesan Tiket")
        print("2. Lihat Semua Tiket")
        print("3. Update Tiket")
        print("4. Hapus Tiket")
        print("5. Cari Tiket")
        print("6. Urutkan Tiket berdasarkan Jam")
        print("7. Lihat Antrian Pembeli")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            create_ticket()
        elif pilihan == "2":
            read_tickets()
        elif pilihan == "3":
            update_ticket()
        elif pilihan == "4":
            delete_ticket()
        elif pilihan == "5":
            search_ticket()
        elif pilihan == "6":
            sort_tickets()
        elif pilihan == "7":
            print("Antrian:", list(antrian))
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid!")

menu()
