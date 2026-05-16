class QueueArray:
    def __init__(self, max_size=100):
        self.MAXN = max_size
        self.q = [None] * self.MAXN
        self.front_idx = -1
        self.rear_idx = -1

    def is_empty(self):
        return self.front_idx == -1

    def is_full(self):
        return (self.rear_idx + 1) % self.MAXN == self.front_idx

    # Menambahkan mata kuliah ke queue
    def enqueue(self, mata_kuliah):
        if self.is_full():
            print("Queue penuh")
            return

        if self.is_empty():
            self.front_idx = 0
            self.rear_idx = 0
        else:
            self.rear_idx = (self.rear_idx + 1) % self.MAXN

        self.q[self.rear_idx] = mata_kuliah
        print(f"Tugas dari mata kuliah {mata_kuliah} berhasil ditambahkan")

    # Menghapus tugas pertama
    def dequeue(self):
        if self.is_empty():
            print("Queue kosong")
            return

        print(f"Tugas dari mata kuliah {self.q[self.front_idx]} berhasil dihapus")

        if self.front_idx == self.rear_idx:
            self.front_idx = -1
            self.rear_idx = -1
        else:
            self.front_idx = (self.front_idx + 1) % self.MAXN

    # Melihat tugas paling depan
    def peek(self):
        if self.is_empty():
            print("Queue kosong")
            return

        print(f"Tugas paling depan berasal dari mata kuliah: {self.q[self.front_idx]}")

    # Menampilkan seluruh isi queue
    def display(self):
        if self.is_empty():
            print("Queue kosong")
            return

        print("\nDaftar Tugas Kuliah:")
        i = self.front_idx
        no = 1

        while True:
            print(f"{no}. {self.q[i]}")

            if i == self.rear_idx:
                break

            i = (i + 1) % self.MAXN
            no += 1


def main():
    queue = QueueArray()
    pilih = 0

    while pilih != 5:
        print("\n=== QUEUE LIST TUGAS KULIAH ===")
        print("1. Tambah Tugas")
        print("2. Hapus Tugas")
        print("3. Lihat Tugas Depan")
        print("4. Tampilkan Semua Tugas")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            matkul = input("Masukkan nama mata kuliah: ")
            queue.enqueue(matkul)

        elif pilih == 2:
            queue.dequeue()

        elif pilih == 3:
            queue.peek()

        elif pilih == 4:
            queue.display()

        elif pilih == 5:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()