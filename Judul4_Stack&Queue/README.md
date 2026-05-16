Judul Program : Implementasi Queue untuk Daftar Tugas Kuliah Menggunakan Python

Program tersebut dibuat menggunakan bahasa pemrograman Python untuk menerapkan struktur data queue atau antrian. Queue bekerja dengan konsep FIFO (First In First Out), yaitu data yang pertama masuk akan menjadi data pertama yang keluar. Pada program ini, queue digunakan untuk menyimpan daftar tugas berdasarkan nama mata kuliah. Program memiliki beberapa fitur seperti menambahkan tugas (enqueue), menghapus tugas (dequeue), melihat tugas paling depan (peek), dan menampilkan seluruh daftar tugas (display).

Queue pada program ini dibuat menggunakan array dengan konsep circular queue, sehingga penyimpanan data menjadi lebih efisien. Program juga dilengkapi dengan pengecekan kondisi queue penuh dan queue kosong agar tidak terjadi kesalahan saat menambahkan atau menghapus data. Penggunaan class QueueArray membuat program lebih rapi dan mudah dipahami karena setiap fungsi queue dipisahkan ke dalam method masing-masing.

<img width="1671" height="618" alt="Screenshot 2026-05-16 183024" src="https://github.com/user-attachments/assets/146a2392-c390-4fcc-998b-7178ff693750" />
<img width="1682" height="458" alt="Screenshot 2026-05-16 183046" src="https://github.com/user-attachments/assets/5040fd63-4cff-4189-b9f6-b22bb3b0c4bf" />
<img width="1683" height="420" alt="Screenshot 2026-05-16 183057" src="https://github.com/user-attachments/assets/52505a79-6a21-45a1-8a7e-48199f9b3726" />
<img width="1682" height="421" alt="Screenshot 2026-05-16 183112" src="https://github.com/user-attachments/assets/02cc8942-1cbc-433d-925e-b2ab9738f7e0" />
<img width="1699" height="529" alt="Screenshot 2026-05-16 183122" src="https://github.com/user-attachments/assets/63dd7fc4-0396-47cc-b836-469a57ad04c7" />

Penjelasan Coding :

class QueueArray:

Membuat class bernama QueueArray untuk implementasi struktur data Queue menggunakan array.

def __init__(self, max_size=100):

Method constructor yang otomatis dijalankan saat objek dibuat.
max_size=100 berarti ukuran maksimum queue adalah 100 data.

self.MAXN = max_size

Menyimpan ukuran maksimum queue ke variabel MAXN.

self.q = [None] * self.MAXN

Membuat list/array dengan isi awal None sebanyak ukuran maksimum queue.

self.front_idx = -1

Variabel penunjuk indeks depan queue.
-1 menandakan queue masih kosong.

self.rear_idx = -1

Variabel penunjuk indeks belakang queue.
-1 juga berarti queue kosong.

def is_empty(self):

Fungsi untuk mengecek apakah queue kosong.

return self.front_idx == -1

Jika front_idx bernilai -1, maka queue kosong dan menghasilkan True.

def is_full(self):

Fungsi untuk mengecek apakah queue penuh.

return (self.rear_idx + 1) % self.MAXN == self.front_idx

Menggunakan konsep circular queue.
Jika posisi setelah rear_idx sama dengan front_idx, maka queue penuh.
Operator % digunakan agar indeks kembali ke awal array jika sudah mencapai batas akhir.

def enqueue(self, mata_kuliah):

Method untuk menambahkan data ke queue.

if self.is_full():

Mengecek apakah queue penuh.

print("Queue penuh")

Menampilkan pesan jika queue penuh.

return

Menghentikan proses enqueue.

if self.is_empty():

Mengecek apakah queue masih kosong.

self.front_idx = 0

Jika kosong, indeks depan diisi 0.

self.rear_idx = 0

Indeks belakang juga diisi 0.

else:

Jika queue tidak kosong.

self.rear_idx = (self.rear_idx + 1) % self.MAXN

Indeks belakang maju satu langkah.

Jika sudah di akhir array, kembali ke awal karena menggunakan modulo %.

self.q[self.rear_idx] = mata_kuliah

Memasukkan data mata kuliah ke array queue.

print(f"Tugas dari mata kuliah {mata_kuliah} berhasil ditambahkan")

Menampilkan pesan bahwa data berhasil ditambahkan.

def dequeue(self):

Method untuk menghapus data paling depan queue.

if self.is_empty():

Mengecek apakah queue kosong.

print("Queue kosong")

Menampilkan pesan queue kosong.

return

Menghentikan proses penghapusan.

print(f"Tugas dari mata kuliah {self.q[self.front_idx]} berhasil dihapus")

Menampilkan data yang dihapus dari posisi depan queue.

if self.front_idx == self.rear_idx:

Mengecek apakah queue hanya memiliki satu data.

self.front_idx = -1
self.rear_idx = -1

Jika hanya satu data, maka queue dikosongkan kembali.

else:

Jika data lebih dari satu.

self.front_idx = (self.front_idx + 1) % self.MAXN

Indeks depan maju satu langkah.

def peek(self):

Method untuk melihat data paling depan tanpa menghapusnya.

if self.is_empty():

Mengecek apakah queue kosong.

print("Queue kosong")

return

print(f"Tugas paling depan berasal dari mata kuliah: {self.q[self.front_idx]}")

Menampilkan data paling depan queue.

def display(self):

Method untuk menampilkan seluruh isi queue.

if self.is_empty():

Mengecek apakah queue kosong.

print("Queue kosong")

Menampilkan pesan queue kosong.

return

Menghentikan proses display.

print("\nDaftar Tugas Kuliah:")

Menampilkan judul daftar tugas.

i = self.front_idx

Variabel i digunakan untuk traversal mulai dari depan queue.

no = 1

Nomor urut daftar tugas.

while True:

Perulangan tanpa batas sampai dihentikan break.

print(f"{no}. {self.q[i]}")

Menampilkan isi queue.

if i == self.rear_idx:

Mengecek apakah sudah sampai data terakhir.

break

Menghentikan perulangan.

i = (i + 1) % self.MAXN

Pindah ke indeks berikutnya.

no += 1

Menambah nomor urut.

def main():

Function utama program.

queue = QueueArray()

Membuat objek queue dari class QueueArray.

pilih = 0

Variabel untuk menyimpan pilihan menu.

while pilih != 5:

Perulangan program selama pengguna belum memilih keluar.

print("\n=== QUEUE LIST TUGAS KULIAH ===")

Menampilkan judul menu.

print("1. Tambah Tugas")
print("2. Hapus Tugas")
print("3. Lihat Tugas Depan")
print("4. Tampilkan Semua Tugas")
print("5. Keluar")

Menampilkan daftar menu.

try:

Mencoba menjalankan input agar aman dari error.

pilih = int(input("Pilih: "))

Meminta input pilihan menu lalu diubah menjadi integer.

except ValueError:

Menangkap error jika input bukan angka.

print("Input tidak valid!")

Menampilkan pesan error input.

continue

Kembali ke awal menu.

if pilih == 1:

Jika memilih menu 1.

matkul = input("Masukkan nama mata kuliah: ")

Meminta input nama mata kuliah.

queue.enqueue(matkul)

Menambahkan data ke queue.

elif pilih == 2:

Jika memilih menu 2.

queue.dequeue()

Menghapus data paling depan.

elif pilih == 3:

Jika memilih menu 3.

queue.peek()

Menampilkan data paling depan.

elif pilih == 4:

Jika memilih menu 4.

queue.display()

Menampilkan seluruh data queue.

elif pilih == 5:

Jika memilih menu keluar.

print("Program selesai.")

Menampilkan pesan program selesai.

else:

Jika pilihan selain 1–5.

print("Pilihan tidak valid!")

Menampilkan pesan pilihan salah.

if __name__ == "__main__":

Mengecek apakah file dijalankan langsung.

main()

Menjalankan function main().

Output :

<img width="1706" height="705" alt="Screenshot 2026-05-16 184959" src="https://github.com/user-attachments/assets/80e31da8-9cb2-47ae-86d0-6562b52313da" />
<img width="1712" height="364" alt="Screenshot 2026-05-16 185014" src="https://github.com/user-attachments/assets/4091943f-d991-49f4-aefe-e44f1377cd19" />
<img width="1721" height="213" alt="Screenshot 2026-05-16 185029" src="https://github.com/user-attachments/assets/d2412055-f76f-4f2b-8fc5-06b7626de44c" />

Link Video Youtube Presentasi : https://youtu.be/WhrrViDrK94
