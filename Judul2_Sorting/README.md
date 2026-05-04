Judul Program : Program Pengurutan Tinggi Pohon Sawit menggunakan Bubble Sort dalam Python

Program ini dibuat untuk mengolah data tinggi pohon sawit yang dimasukkan oleh pengguna, lalu mengurutkannya dari yang paling tinggi ke yang paling rendah menggunakan algoritma Bubble Sort. Data yang diinput tidak hanya berupa tinggi pohon saja, tetapi juga disimpan bersama nomor urutnya dalam bentuk pasangan (tuple), supaya identitas tiap pohon tetap jelas meskipun sudah diurutkan. Di awal, program meminta jumlah data yang akan dimasukkan, kemudian pengguna menginput tinggi masing-masing pohon. Selain itu, program juga dilengkapi dengan penanganan error agar input yang diterima benar-benar berupa angka.

Setelah semua data terkumpul, proses pengurutan dilakukan dengan metode Bubble Sort, yaitu dengan membandingkan elemen yang berdekatan lalu menukarnya jika posisinya belum sesuai. Setelah proses selesai, hasilnya ditampilkan dengan format yang rapi, menampilkan nomor pohon beserta tingginya dalam satuan meter. Dengan begitu, pengguna bisa dengan mudah melihat urutan pohon dari yang tertinggi sampai yang terendah.

<img width="1642" height="106" alt="Screenshot 2026-05-04 113511" src="https://github.com/user-attachments/assets/892bb4a5-d0b5-43cf-bb2c-3ebabe7d790a" />
<img width="1638" height="133" alt="Screenshot 2026-05-04 113533" src="https://github.com/user-attachments/assets/257ea04d-ca77-493d-bb92-30f98c5b8701" />
<img width="1657" height="756" alt="Screenshot 2026-05-04 113615" src="https://github.com/user-attachments/assets/abc9596b-5431-455f-807a-6697053d296d" />

Penjelasan Coding :

def tukar(arr, i, j):

Mendefinisikan fungsi untuk menukar posisi dua elemen dalam array.

temp = arr[i]

Menyimpan sementara nilai pada index i.

arr[i] = arr[j]

Mengganti nilai index i dengan nilai dari index j.

arr[j] = temp

Mengisi index j dengan nilai yang tadi disimpan di temp.

def bubble_sort(arr, n):

Mendefinisikan fungsi untuk mengurutkan array menggunakan Bubble Sort.

for i in range(n - 1):

Perulangan luar untuk menentukan jumlah tahap sorting (n-1 tahap).

for j in range(n - i - 1):

Perulangan dalam untuk membandingkan elemen yang bersebelahan.

if arr[j][1] < arr[j + 1][1]:

Membandingkan tinggi pohon, jika lebih kecil dari sebelahnya maka perlu ditukar (descending).

tukar(arr, j, j + 1)

Memanggil fungsi tukar untuk menukar posisi kedua elemen.

def main():

Fungsi utama program.

try:
n = int(input("Masukkan jumlah pohon sawit: "))

Meminta input jumlah pohon dari user.

except ValueError:
print("Input tidak valid!")
return

Menangani error jika input bukan angka.

arr = []

Membuat list kosong untuk menyimpan data pohon.

print("Masukkan tinggi pohon (dalam meter):")

Menampilkan instruksi ke user.

for i in range(n):

Perulangan untuk input data sebanyak n.

while True:

Loop agar input valid (akan mengulang jika salah).

try:
tinggi = int(input(f"Pohon ke-{i+1}: "))

Mengambil input tinggi pohon ke-(i+1).

arr.append((i + 1, tinggi))

Menyimpan data dalam bentuk tuple.

break

Keluar dari loop jika input valid.

except ValueError:
print("Input tidak valid, silakan masukkan angka!")

Menangani jika user salah input.

print("\nData sebelum diurutkan:")
print(arr)

Menampilkan data sebelum sorting.

bubble_sort(arr, n)

Memanggil fungsi Bubble Sort untuk mengurutkan data.

print("\nHasil pengurutan tinggi pohon (tertinggi ke terendah):")

Menampilkan judul output hasil sorting.

for nomor, tinggi in arr:

Loop untuk membaca isi tuple.

print(f"Pohon ke-{nomor} ({tinggi}m)")

Menampilkan output sesuai format yang diinginkan.

if __name__ == "__main__":

Mengecek apakah file dijalankan langsung (bukan di-import).

main()

Memanggil fungsi main() untuk menjalankan program.


Output :

<img width="1676" height="434" alt="Screenshot 2026-05-04 184352" src="https://github.com/user-attachments/assets/da127a2e-1fdd-4a45-8eda-b08b69374f56" />
