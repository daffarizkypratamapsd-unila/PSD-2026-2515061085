Judul Program : Program Mencari Barang pada Gudang berdasarkan Nomor Barang menggunakan Sequential Search Sentinel pada Python

Program ini dibuat untuk membantu petugas gudang dalam mencari nomor barang secara cepat menggunakan metode Sequential Search Sentinel. Data nomor barang disimpan dalam sebuah list, kemudian pengguna diminta memasukkan nomor barang yang ingin dicari. Sistem akan melakukan pencarian satu per satu dari awal data hingga menemukan nomor barang yang sesuai. Jika nomor barang ditemukan, program akan menampilkan posisi indeks barang tersebut, sedangkan jika tidak ditemukan maka program akan memberikan informasi bahwa nomor barang tidak tersedia di gudang.

Metode Sequential Search Sentinel bekerja dengan menambahkan sementara nilai yang dicari ke bagian akhir list sebagai penanda (sentinel). Teknik ini membuat proses pencarian menjadi lebih efisien karena perulangan tidak perlu terus-menerus memeriksa batas akhir array. Setelah proses pencarian selesai, nilai sentinel akan dihapus kembali sehingga data tetap seperti semula. Program juga dilengkapi dengan validasi input agar pengguna hanya dapat memasukkan angka, sehingga mengurangi kemungkinan terjadinya kesalahan saat program dijalankan.

<img width="1671" height="265" alt="Screenshot 2026-05-09 174730" src="https://github.com/user-attachments/assets/a9780d87-7afb-4d12-afae-e48f7a327f5e" />
<img width="1671" height="587" alt="Screenshot 2026-05-09 174901" src="https://github.com/user-attachments/assets/38e787e5-6591-440d-ada3-448391a64e27" />

Penjelasan Coding :

def sequential_search_sentinel(data_barang, n, target):

Baris ini digunakan untuk membuat fungsi bernama sequential_search_sentinel dengan 3 parameter yaitu data_barang, n, dan target.

data_barang.append(target)

Baris ini menambahkan nilai target ke akhir list sebagai sentinel atau penanda sementara

i = 0

Membuat variabel i dengan nilai awal 0 yang digunakan sebagai indeks untuk melakukan pencarian dari data pertama.

while data_barang[i] != target:

Perulangan while akan terus berjalan selama data pada indeks i belum sama dengan nilai target.

i += 1

Jika data belum cocok, maka indeks i ditambah 1 agar pencarian berpindah ke data berikutnya.

data_barang.pop()

Setelah pencarian selesai, sentinel yang tadi ditambahkan di akhir list akan dihapus kembali menggunakan pop().

if i < n:

Mengecek apakah indeks i masih berada di dalam jumlah data asli.

return True, i

Jika target ditemukan, fungsi mengembalikan True dan i

else:

Jika kondisi sebelumnya salah, maka program masuk ke bagian else.

return False, -1

Jika target tidak ditemukan, maka mengembalikan false dan i = -1

def main():

Membuat fungsi utama bernama main() yang digunakan untuk menjalankan program.

data_barang = [103, 108, 101, 109, 100, 106, 107, 105, 112, 102]

Membuat list berisi data nomor barang di gudang.

n = len(data_barang)

Menghitung jumlah data dalam list menggunakan fungsi len() lalu menyimpannya ke variabel n.

print(f"Daftar nomor barang: {data_barang}")

Menampilkan seluruh data nomor barang yang tersedia.

while True:

Membuat perulangan

try:

Digunakan untuk menangani kemungkinan error saat input.

target = int(input("Masukkan nomor barang yang ingin dicari: "))

Meminta pengguna memasukkan nomor barang yang ingin dicari lalu mengubah input menjadi tipe integer.

break

Jika input benar, perulangan dihentikan.

except ValueError:

Bagian ini dijalankan jika pengguna memasukkan selain angka.

print("Input tidak valid! Masukkan angka.")

Menampilkan pesan kesalahan jika input bukan angka.

found, index = sequential_search_sentinel(data_barang, n, target)

Memanggil fungsi sequential_search_sentinel() untuk mencari data, lalu hasilnya disimpan ke variabel

if found:

Mengecek apakah data berhasil ditemukan.

print(f"Barang nomor {target} ditemukan pada posisi indeks ke-{index}")

Jika ditemukan, program menampilkan nomor barang beserta posisi indeksnya.

else:

Jika data tidak ditemukan, program masuk ke bagian else.

print(f"Barang nomor {target} tidak ditemukan dalam gudang")

Menampilkan pesan bahwa nomor barang tidak tersedia.

if __name__ == "__main__":

Mengecek apakah file Python dijalankan langsung sebagai program utama.

main()

Menjalankan fungsi main() sehingga seluruh program dapat berjalan.

Output :

<img width="1652" height="140" alt="Screenshot 2026-05-09 180020" src="https://github.com/user-attachments/assets/0670af46-13d4-4b91-bcf4-756d3d5ccf45" />

Link Video Presentasi Youtube : 
