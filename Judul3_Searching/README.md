Judul Program : Program Mencari Barang pada Gudang berdasarkan Nomor Barang menggunakan Sequential Search Sentinel pada Python

Program ini dibuat untuk membantu petugas gudang dalam mencari nomor barang secara cepat menggunakan metode Sequential Search Sentinel. Data nomor barang disimpan dalam sebuah list, kemudian pengguna diminta memasukkan nomor barang yang ingin dicari. Sistem akan melakukan pencarian satu per satu dari awal data hingga menemukan nomor barang yang sesuai. Jika nomor barang ditemukan, program akan menampilkan posisi indeks barang tersebut, sedangkan jika tidak ditemukan maka program akan memberikan informasi bahwa nomor barang tidak tersedia di gudang.

Metode Sequential Search Sentinel bekerja dengan menambahkan sementara nilai yang dicari ke bagian akhir list sebagai penanda (sentinel). Teknik ini membuat proses pencarian menjadi lebih efisien karena perulangan tidak perlu terus-menerus memeriksa batas akhir array. Setelah proses pencarian selesai, nilai sentinel akan dihapus kembali sehingga data tetap seperti semula. Program juga dilengkapi dengan validasi input agar pengguna hanya dapat memasukkan angka, sehingga mengurangi kemungkinan terjadinya kesalahan saat program dijalankan.

<img width="1671" height="265" alt="Screenshot 2026-05-09 174730" src="https://github.com/user-attachments/assets/a9780d87-7afb-4d12-afae-e48f7a327f5e" />
<img width="1671" height="587" alt="Screenshot 2026-05-09 174901" src="https://github.com/user-attachments/assets/38e787e5-6591-440d-ada3-448391a64e27" />

Penjelasan Coding :

