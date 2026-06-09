Judul Program : Implementasi Hash Map dengan Metode Separate Chaining untuk Sistem Pendataan Kandang Ayam pada Peternakan

Program ini merupakan implementasi struktur data Hash Map menggunakan metode Separate Chaining untuk mengelola data kandang ayam pada sebuah peternakan. Setiap kandang memiliki ID Kandang sebagai key dan jumlah ayam sebagai value. Hash Map digunakan untuk mempercepat proses penyimpanan, pencarian, dan penghapusan data kandang berdasarkan ID yang dimiliki masing-masing kandang.

Metode Separate Chaining digunakan untuk mengatasi masalah collision, yaitu kondisi ketika beberapa ID kandang menghasilkan indeks hash yang sama. Dalam metode ini, data yang memiliki indeks sama disimpan dalam bentuk linked list. Program menyediakan fitur untuk menambahkan data kandang, mencari data berdasarkan ID kandang, menghapus data kandang, serta menampilkan seluruh data yang tersimpan dalam hash table.

<img width="1703" height="666" alt="Screenshot 2026-06-09 165624" src="https://github.com/user-attachments/assets/54d1faa4-94bd-465b-aba2-02766018c988" />
<img width="1711" height="693" alt="Screenshot 2026-06-09 165643" src="https://github.com/user-attachments/assets/8b6bf6f6-e412-46c4-895d-012321bcbbe7" />
<img width="1712" height="361" alt="Screenshot 2026-06-09 165657" src="https://github.com/user-attachments/assets/6585bb6e-22c9-402c-8162-c0ec71f73dfd" />
<img width="1707" height="717" alt="Screenshot 2026-06-09 165710" src="https://github.com/user-attachments/assets/d78d684c-5848-4049-84f9-785988a8acf4" />

Penjelasan Coding :

class Node:

Membuat kelas Node yang akan digunakan sebagai elemen pada linked list

def __init__(self, id_kandang, jumlah_ayam):

Constructor yang dijalankan saat objek Node dibuat.

self.key = id_kandang

Menyimpan ID kandang sebagai key.

self.value = jumlah_ayam

Menyimpan jumlah ayam sebagai value.

self.next = None

Pointer ke node berikutnya. Awalnya kosong (None).

class HashMapKandangAyam:

Membuat kelas Hash Map untuk menyimpan data kandang ayam.

def __init__(self, size=10):

Constructor kelas Hash Map.

self.SIZE = size

Menentukan ukuran tabel hash sebanyak 10.

self.table = [None] * self.SIZE

Membuat list berisi 10 elemen kosong.

def hash_function(self, id_kandang):

Fungsi untuk menentukan posisi penyimpanan data.

return (id_kandang % self.SIZE + self.SIZE) % self.SIZE

Menggunakan operasi modulo.

def tambah_kandang(self, id_kandang, jumlah_ayam):

Fungsi untuk menambahkan data baru.

index = self.hash_function(id_kandang)

Mencari tempat data disimpan.

current = self.table[index]

Mengambil node pertama pada bucket tersebut.

while current is not None:

Melakukan pengecekan apakah node sudah ada.

if current.key == id_kandang:

Jika ID kandang sudah ada.

current.value = jumlah_ayam

Update jumlah ayam.

return

Keluar dari fungsi.

new_node = Node(id_kandang, jumlah_ayam)

Membuat node baru.

new_node.next = self.table[index]

Menghubungkan node baru ke node lama.

self.table[index] = new_node

Menjadikan node baru sebagai node pertama.

def cari_kandang(self, id_kandang):

Fungsi mencari data berdasarkan ID.

index = self.hash_function(id_kandang)

Menentukan tempat.

current = self.table[index]

Mengambil node pertama.

while current is not None:

Menelusuri linked list.

if current.key == id_kandang:

Jika ID ditemukan.

return current

Mengembalikan node tersebut.

current = current.next

Pindah ke node berikutnya.

return None

Jika tidak ditemukan.

def hapus_kandang(self, id_kandang):

Fungsi untuk menghapus data.

index = self.hash_function(id_kandang)

Mencari tempat.

current = self.table[index]

Node yang sedang diperiksa.

prev = None

Menyimpan node sebelumnya.

while current is not None:

if current.key == id_kandang:

Jika ID ditemukan.

if prev is None:
                    self.table[index] = current.next

Jika node pertama

else:
                    prev.next = current.next

Jika node di tengah

return True

Menandakan penghapusan berhasil.

prev = current
current = current.next

Maju ke node berikutnya.

return False

Jika data tidak ditemukan.

def tampilkan_data(self):

Menampilkan isi Hash Map.

print("\nData Kandang Ayam:")

Menampilkan judul.

for i in range(self.SIZE):

Melakukan perulangan dari 0 sampai 9.

print(f"Bucket {i}: ", end="")

Menampilkan nomor.

current = self.table[i]

Mengambil node pertama.

while current is not None:

Menelusuri linked list.

print(
      f"[ID Kandang:{current.key}, Jumlah Ayam:{current.value}] -> ",
      end=""
    )

Menampilkan data kandang.

current = current.next

Pindah ke node berikutnya.

print("NULL")

def main():

Program utama.

peternakan = HashMapKandangAyam()

Membuat objek Hash Map.

peternakan.tambah_kandang(101, 150)

Kandang 101 berisi 150 ayam.

peternakan.tambah_kandang(111, 200)

Kandang 111 berisi 200 ayam.

peternakan.tambah_kandang(121, 175)

Kandang 121 berisi 175 ayam.

peternakan.tambah_kandang(102, 120)

Kandang 102 berisi 120 ayam.

peternakan.tampilkan_data()

Menampilkan seluruh data

hasil = peternakan.cari_kandang(111)

Mencari kandang

if hasil:

Jika ditemukan

print(
      f"\nKandang ID {hasil.key} ditemukan "
      f"dengan jumlah ayam {hasil.value} ekor"
)

Menampilkan hasil pencarian.

peternakan.hapus_kandang(111)

Menghapus kandang ID 111.

peternakan.tampilkan_data()

Menampilkan data setelah penghapusan

Output :
<img width="1826" height="686" alt="Screenshot 2026-06-09 171400" src="https://github.com/user-attachments/assets/a05fe5da-8cb4-4403-b466-33fa5012cba4" />

Link Video Presentasi Youtube : https://youtu.be/RrgSydu1iUw
