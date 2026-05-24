Judul Program : Implementasi Binary Search Tree pada Sistem Pengelolaan Nomor Buku Perpustakaan

Program ini merupakan implementasi struktur data Binary Search Tree (BST) dalam sistem pengelolaan nomor buku perpustakaan. Program digunakan untuk menyimpan data nomor buku secara terstruktur sehingga proses penambahan, pencarian, dan penghapusan data dapat dilakukan dengan lebih cepat dan efisien.

Program menyediakan beberapa fitur utama, seperti menambahkan nomor buku, menghapus nomor buku, menampilkan data buku menggunakan metode level-order, mencari tinggi pohon BST, serta mencari successor dan predecessor dari suatu nomor buku. Dengan adanya fitur-fitur tersebut, program dapat membantu perpustakaan dalam mengelola data buku secara lebih teratur.

<img width="1715" height="118" alt="Screenshot 2026-05-24 102449" src="https://github.com/user-attachments/assets/f41b0c19-cd29-4376-bb00-fb0f59064582" />
<img width="1719" height="352" alt="Screenshot 2026-05-24 102503" src="https://github.com/user-attachments/assets/1a8b00e0-60d3-43a8-a590-9d6fedec9ecd" />
<img width="1716" height="282" alt="Screenshot 2026-05-24 102515" src="https://github.com/user-attachments/assets/c0ed8a3e-3426-4a5f-9aa0-87de1808e003" />
<img width="1703" height="229" alt="Screenshot 2026-05-24 102527" src="https://github.com/user-attachments/assets/90a5be18-655f-4ddb-b989-07a9370b69db" />
<img width="1718" height="455" alt="Screenshot 2026-05-24 102545" src="https://github.com/user-attachments/assets/eb7b1991-cf42-44c1-9269-9cdba153efe6" />
<img width="1698" height="265" alt="Screenshot 2026-05-24 102556" src="https://github.com/user-attachments/assets/ebf601d4-3b63-4c47-b27e-b3746d792308" />
<img width="1707" height="475" alt="Screenshot 2026-05-24 102606" src="https://github.com/user-attachments/assets/4fa75035-77bd-4c1f-a0f0-9ec11c9338bb" />
<img width="1713" height="353" alt="Screenshot 2026-05-24 102616" src="https://github.com/user-attachments/assets/29b7531f-cbc3-4085-b42e-bcfedbe09ab5" />
<img width="1710" height="259" alt="Screenshot 2026-05-24 102626" src="https://github.com/user-attachments/assets/25395ce3-c116-4fb5-9d7d-5932d2870ae8" />
<img width="1719" height="342" alt="Screenshot 2026-05-24 102636" src="https://github.com/user-attachments/assets/711ac6b7-e246-4e01-b2c4-adce73fc9c65" />
<img width="1715" height="380" alt="Screenshot 2026-05-24 102643" src="https://github.com/user-attachments/assets/4ef5f0fd-598a-4640-b54d-4508d852964a" />
<img width="1711" height="322" alt="Screenshot 2026-05-24 102653" src="https://github.com/user-attachments/assets/350caf24-ec88-46d9-933c-da4663c90495" />
<img width="1711" height="399" alt="Screenshot 2026-05-24 102704" src="https://github.com/user-attachments/assets/dc0a53b8-d0a1-4481-9800-db15cc880f1d" />
<img width="1704" height="323" alt="Screenshot 2026-05-24 102712" src="https://github.com/user-attachments/assets/cc06e09e-f8f3-4c21-b976-0d68d6767bbc" />
<img width="1701" height="134" alt="Screenshot 2026-05-24 102723" src="https://github.com/user-attachments/assets/048cf311-d100-45f2-8e73-23d9bc0848ae" />
<img width="1708" height="421" alt="Screenshot 2026-05-24 102733" src="https://github.com/user-attachments/assets/d05a8598-ab1d-4d2b-8dee-9101a9841d75" />
<img width="1728" height="399" alt="Screenshot 2026-05-24 102742" src="https://github.com/user-attachments/assets/0e67c3ca-ecfc-4ff7-99a8-d4fc73862b00" />
<img width="1706" height="218" alt="Screenshot 2026-05-24 102750" src="https://github.com/user-attachments/assets/e5f17aff-c00b-4c84-b254-58498fb263fd" />

Penjelasan Coding :

class Buku:

Membuat class bernama Buku untuk merepresentasikan node pada Binary Search Tree.

def __init__(self, nomor_buku):

Constructor class Buku yang dijalankan saat objek dibuat.

self.nomor_buku = nomor_buku

Menyimpan nilai nomor buku ke dalam node.

self.left = None

Membuat child kiri dengan nilai awal None.

self.right = None

Membuat child kanan dengan nilai awal None.

class BSTPerpustakaan:

Membuat class Binary Search Tree untuk sistem perpustakaan.

def __init__(self):

Constructor class BST.

self.root = None

Menyimpan root awal BST dengan nilai kosong.

def tambah_buku_node(self, root, nomor_buku):

Function rekursif untuk menambahkan node baru.

if root is None:

Mengecek apakah posisi node masih kosong.

return Buku(nomor_buku)

Jika kosong, buat node baru.

if nomor_buku < root.nomor_buku:

Mengecek apakah nomor buku lebih kecil dari root.

root.left = self.tambah_buku_node(root.left, nomor_buku)

Menambahkan data ke subtree kiri.

elif nomor_buku > root.nomor_buku:

Mengecek apakah nomor buku lebih besar dari root.

root.right = self.tambah_buku_node(root.right, nomor_buku)

Menambahkan data ke subtree kanan.

return root

Mengembalikan node root.

def tambah_buku(self, nomor_buku):

Function untuk memanggil proses insert.

self.root = self.tambah_buku_node(self.root, nomor_buku)

Menambahkan data mulai dari root.

def cari_buku_terkecil(self, root):

Function mencari node dengan nilai terkecil.

current = root

Variabel sementara untuk traversal.

while current is not None and current.left is not None:

Loop selama masih ada child kiri.

current = current.left

Berpindah ke node paling kiri.

return current

Mengembalikan node terkecil.

def hapus_buku_node(self, root, nomor_buku):

Function rekursif untuk menghapus node.

if root is None:

Jika tree kosong.

return None

Mengembalikan nilai kosong.

if nomor_buku < root.nomor_buku:

Jika nilai lebih kecil dari root.

root.left = self.hapus_buku_node(root.left, nomor_buku)

Cari node di subtree kiri.

elif nomor_buku > root.nomor_buku:

Jika nilai lebih besar dari root.

root.right = self.hapus_buku_node(root.right, nomor_buku)

Cari node di subtree kanan.

else:

Jika node ditemukan.

if root.left is None and root.right is None:

Jika node tidak memiliki child.

return None

Node langsung dihapus.

elif root.left is None:

Jika hanya memiliki child kanan.

return root.right

Ganti node dengan child kanan.

elif root.right is None:

Jika hanya memiliki child kiri.

return root.left

Ganti node dengan child kiri.

else:

Jika node memiliki dua child.

pengganti = self.cari_buku_terkecil(root.right)

Mencari successor.

root.nomor_buku = pengganti.nomor_buku

Mengganti nilai node dengan successor.

root.right = self.hapus_buku_node(
                    root.right,
                    pengganti.nomor_buku
                )

Menghapus node successor lama.

return root

Mengembalikan root terbaru.

def hapus_buku(self, nomor_buku):

Function utama delete.

self.root = self.hapus_buku_node(self.root, nomor_buku)

Memulai proses delete dari root.

def tinggi_pohon(self, root):

Function mencari tinggi BST.

if root is None:

Jika node kosong.

return -1

Mengembalikan -1.

kiri = self.tinggi_pohon(root.left)

Menghitung tinggi subtree kiri.

kanan = self.tinggi_pohon(root.right)

Menghitung tinggi subtree kanan.

return 1 + max(kiri, kanan)

Mengambil tinggi terbesar lalu ditambah 1.

def tampil_level_order(self, root):

Function traversal level-order.

if root is None:

Jika tree kosong.

print("(Data buku kosong)")

Menampilkan pesan kosong.

return

Menghentikan function.

queue = []

Membuat queue.

queue.append(root)

Menambahkan root ke queue.

while len(queue) > 0:

Loop selama queue tidak kosong.

current = queue.pop(0)

Mengambil elemen pertama queue.

print(current.nomor_buku, end=" ")

Menampilkan nomor buku.

if current.left is not None:

Jika ada child kiri.

queue.append(current.left)

Masukkan child kiri ke queue.

if current.right is not None:

Jika ada child kanan.

queue.append(current.right)

Masukkan child kanan ke queue.

print()

Pindah baris.

def cari_successor(self, root, nomor_buku):

Function mencari successor.

current = root

Memulai traversal dari root.

successor = None

Variabel penyimpan successor.

while current is not None:

Loop pencarian node.

if nomor_buku < current.nomor_buku:

Jika nilai lebih kecil.

successor = current

Simpan kandidat successor.

current = current.left

Berpindah ke kiri.

elif nomor_buku > current.nomor_buku:

Jika nilai lebih besar.

current = current.right

Berpindah ke kanan.

else:

Jika node ditemukan.

break

Keluar loop.

if current is None:

Jika node tidak ditemukan.

return None, False

Mengembalikan gagal.

if current.right is not None:

Jika memiliki subtree kanan.

successor = self.cari_buku_terkecil(current.right)

Cari nilai terkecil di subtree kanan.

if successor is None:

Jika successor tidak ada.

return None, False

Mengembalikan gagal.

return successor.nomor_buku, True

Mengembalikan successor.

def cari_predecessor(self, root, nomor_buku):

Function mencari predecessor.

current = root

Mulai traversal dari root.

predecessor = None

Variabel penyimpan predecessor.

while current is not None:

Loop pencarian.

if nomor_buku > current.nomor_buku:

Jika nilai lebih besar.

predecessor = current

Simpan kandidat predecessor.

current = current.right

Berpindah ke kanan.

elif nomor_buku < current.nomor_buku:

Jika nilai lebih kecil.

current = current.left

Berpindah ke kiri.

else:

Jika node ditemukan.

break

Keluar loop.

if current is None:

Jika node tidak ditemukan.

return None, False

Mengembalikan gagal.

if current.left is not None:

Jika memiliki subtree kiri.

temp = current.left

Traversal ke subtree kiri.

while temp.right is not None:

Mencari node paling kanan.

temp = temp.right

Berpindah ke kanan.

predecessor = temp

Simpan predecessor.

if predecessor is None:

Jika predecessor tidak ada.

return None, False

Mengembalikan gagal.

return predecessor.nomor_buku, True

Mengembalikan predecessor.

def main():

Function utama program yang akan dijalankan pertama kali.

perpustakaan = BSTPerpustakaan()

Membuat objek BST bernama perpustakaan.

pilih = 0

Variabel untuk menyimpan pilihan menu pengguna.

 while pilih != 7:

 Perulangan menu selama pengguna belum memilih keluar.

 print("\n=== Sistem BST Perpustakaan ===")

 Menampilkan judul program.

 print("1. Tambah Buku")

 Menampilkan menu tambah buku.

 print("2. Hapus Buku")

 Menampilkan menu hapus buku.

 print("3. Tampilkan Buku (Level-order)")

 Menampilkan menu traversal level-order.

 print("4. Tinggi Pohon")

 Menampilkan menu tinggi pohon BST.

 print("5. Cari Successor Buku")

 Menampilkan menu mencari successor.

 print("6. Cari Predecessor Buku")

 Menampilkan menu mencari predecessor.

 print("7. Keluar")

 Menampilkan menu keluar program.

 try:

 Mencoba menjalankan input pengguna.

 pilih = int(input("Pilih menu: "))

 Meminta pengguna memilih menu dan mengubah input menjadi integer.

 except ValueError:

 Menangani error jika input bukan angka.

 print("Input tidak valid!")

 Menampilkan pesan error.

 continue

 Kembali ke awal perulangan menu.

 if pilih == 1:

 Jika pengguna memilih menu 1.

 try:

 Mencoba membaca input.

 nomor = int(input("Masukkan nomor buku: "))

 Meminta nomor buku dari pengguna.

 perpustakaan.tambah_buku(nomor)

 Menambahkan nomor buku ke BST.

 print(f"Nomor buku {nomor} berhasil ditambahkan")

 Menampilkan pesan berhasil.

 except ValueError:

 Jika input bukan angka.

 print("Input tidak valid!")

 Menampilkan pesan error.

elif pilih == 2:

Jika pengguna memilih menu 2.

try:

Mencoba membaca input.

nomor = int(input("Masukkan nomor buku yang dihapus: "))

Meminta nomor buku yang akan dihapus.

perpustakaan.hapus_buku(nomor)

Menghapus nomor buku dari BST.

print(f"Nomor buku {nomor} berhasil dihapus")

Menampilkan pesan berhasil.

except ValueError:

Jika input salah.

print("Input tidak valid!")

Menampilkan pesan error.

elif pilih == 3:

Jika pengguna memilih menu 3.

print("Data buku: ", end="")

Menampilkan teks awal output traversal.

perpustakaan.tampil_level_order(perpustakaan.root)

Menampilkan data BST menggunakan traversal level-order.

elif pilih == 4:

Jika pengguna memilih menu 4.

print(
                f"Tinggi pohon BST: "
                f"{perpustakaan.tinggi_pohon(perpustakaan.root)}"
            )

Menampilkan tinggi Binary Search Tree.

elif pilih == 5:

Jika pengguna memilih menu 5.

try:

Mencoba membaca input.

nomor = int(input("Cari successor nomor buku: "))

Meminta nomor buku yang ingin dicari successornya.

hasil, found = perpustakaan.cari_successor(
                    perpustakaan.root,
                    nomor
                )

Memanggil function pencarian successor.

if found:

Jika successor ditemukan.

print(f"Successor buku: {hasil}")

Menampilkan hasil successor.

else:

Jika successor tidak ditemukan.

print("Successor tidak ditemukan")

Menampilkan pesan gagal.

except ValueError:

Menangani input salah.

print("Input tidak valid!")

Menampilkan pesan error.

elif pilih == 6:

Jika pengguna memilih menu 6.

try:

Mencoba membaca input.

nomor = int(input("Cari predecessor nomor buku: "))

Meminta nomor buku yang ingin dicari predecessornya.

hasil, found = perpustakaan.cari_predecessor(
                    perpustakaan.root,
                    nomor
                )

Memanggil function pencarian predecessor.

if found:

Jika predecessor ditemukan.

print(f"Predecessor buku: {hasil}")

Menampilkan hasil predecessor.

else:

Jika predecessor tidak ditemukan.

print("Predecessor tidak ditemukan")

Menampilkan pesan gagal.

except ValueError:

Jika input salah.

print("Input tidak valid!")

Menampilkan pesan error.

elif pilih == 7:

Jika pengguna memilih menu keluar.

print("Program selesai")

Menampilkan pesan program selesai.

else:

Jika pilihan menu tidak tersedia.

print("Pilihan tidak valid!")

Menampilkan pesan error pilihan.

if __name__ == "__main__":

Mengecek apakah file dijalankan langsung.

main()

Menjalankan function main().
