Judul Program : Program Pengolahan Nilai Siswa Menggunakan list dalam Python

Program ini merupakan aplikasi sederhana berbasis Python yang digunakan untuk mengolah nilai siswa. Program berjalan secara interaktif melalui menu, di mana pengguna dapat memasukkan lima nilai siswa ke dalam array, menampilkan kembali data yang telah diinput, serta melakukan analisis sederhana seperti menghitung total nilai, rata-rata, nilai tertinggi, dan nilai terendah.

Program ini menggunakan struktur data list. Dalam implementasinya, program memanfaatkan perulangan (while dan for) untuk mengontrol alur dan mengakses setiap elemen array, serta menggunakan validasi input agar data yang dimasukkan harus berupa angka. Selain itu, fungsi bawaan Python seperti sum(), max(), dan min() digunakan untuk mempermudah proses perhitungan, sehingga program ini dapat menjadi contoh dasar dalam memahami pengolahan data menggunakan list secara efisien.

<img width="1722" height="149" alt="Screenshot 2026-04-28 230213" src="https://github.com/user-attachments/assets/747ffb9d-36f3-4ac2-a918-082d3341980b" />
<img width="1696" height="544" alt="Screenshot 2026-04-28 230225" src="https://github.com/user-attachments/assets/b2b8b588-e549-471a-ba34-f28f72c22037" />
<img width="1715" height="723" alt="Screenshot 2026-04-28 230249" src="https://github.com/user-attachments/assets/4c14497c-3887-4328-9bb1-275f452c92c4" />

Penjelasan kode :

def menu():

Mendefinisikan fungsi menu() untuk menampilkan pilihan program.

 print("\n=== MENU ===")
 
Menampilkan judul menu (dengan \n agar ada jarak/baris baru).

  print("1. Masukkan nilai kedalam semua index array")
  print("2. Tampilkan data nilai siswa")
  print("3. Analisis nilai (rata-rata, max, min)")
  print("4. Keluar")
  
Menampilkan daftar pilihan yang bisa dipilih user.

def main():

Mendefinisikan fungsi utama program.

a = [0] * 5

Membuat list (array) berisi 5 elemen dengan nilai awal 0

running = True
Variabel kontrol untuk menjalankan perulangan (loop).

while running:

Loop akan terus berjalan selama running = True

menu()

Memanggil fungsi menu() untuk menampilkan pilihan.

try:
            choice = int(input("Pilihan: "))
            
Meminta input dari user lalu mengubahnya menjadi integer.

except ValueError:

saat user menginputkan angka yang tidak valid maka program tidak error.

  print("Masukkan angka yang valid!")
  
Jika except terpenuhi, maka akan menampilkan teks diatas.

  continue
melewati dan mengulang ke awal loop.

if choice == 1:

Jika user memilih menu 1.

print("Masukkan 5 nilai siswa:")

Menampilkan instruksi input.

for i in range(5):

Perulangan dari indeks 0 sampai 4 (total 5 data).

while True:

Loop validasi agar input harus benar.

try:
              a[i] = int(input(f"Nilai siswa ke-{i+1}: "))
              
Mengisi nilai ke array a pada indeks ke-i.

 break
 
Jika input valid maka keluar dari loop while True.

 except ValueError:
            print("Input tidak valid, masukkan angka!")
            
Jika input bukan angka maka akan menampilkan print dan mengulangi input.

print(f"Data nilai sekarang: {a}")

Menampilkan isi array setelah diinput.

elif choice == 2:

Jika user memilih menu 2.

 print("\n=== DATA NILAI SISWA ===")
 
Menampilkan judul data.

for i in range(5):

Loop untuk menampilkan semua elemen array.

print(f"Siswa ke-{i+1}: {a[i]}")

Menampilkan nilai tiap siswa.

elif choice == 3:

Jika user memilih menu 3.

print("\n=== ANALISIS NILAI ===")

Judul bagian analisis.

total = sum(a)

Menghitung total semua nilai dalam array.

rata = total / len(a)

Menghitung rata-rata.

maksimum = max(a)

Mencari nilai terbesar.

 minimum = min(a)
 
Mencari nilai terkecil.

print(f"Total nilai    : {total}")
print(f"Rata-rata      : {rata}")
print(f"Nilai tertinggi: {maksimum}")
print(f"Nilai terendah : {minimum}")

Menampilkan hasil analisis.

elif choice == 4:

Jika user memilih keluar.

running = False

Menghentikan loop (while akan berhenti).

 print("Program selesai.")
 
Menampilkan pesan selesai.

else:
  print("Pilihan tidak valid!")
  
Menangani input yang tidak sesuai menu.

if __name__ == "__main__":

Menentukan bahwa file ini dijalankan langsung (bukan di-import).

main()

Menjalankan fungsi utama main().

OUTPUT :
<img width="1707" height="287" alt="Screenshot 2026-04-28 231647" src="https://github.com/user-attachments/assets/9d01ada5-5ebd-468a-b9ca-3640d87e9c41" />
<img width="1721" height="292" alt="Screenshot 2026-04-28 231731" src="https://github.com/user-attachments/assets/03f8100c-9b00-48ae-9189-8babfbe67be6" />
<img width="1717" height="276" alt="Screenshot 2026-04-28 231749" src="https://github.com/user-attachments/assets/b932f46d-b3da-478a-9913-17675bf3e730" />

Link Video Presentasi Youtube : https://youtu.be/qo-Y3AAGLd8
