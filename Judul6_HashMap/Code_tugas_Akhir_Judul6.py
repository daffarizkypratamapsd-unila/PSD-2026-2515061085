class Node:
    def __init__(self, id_kandang, jumlah_ayam):
        self.key = id_kandang
        self.value = jumlah_ayam
        self.next = None


class HashMapKandangAyam:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, id_kandang):
        return (id_kandang % self.SIZE + self.SIZE) % self.SIZE

    def tambah_kandang(self, id_kandang, jumlah_ayam):
        index = self.hash_function(id_kandang)

        current = self.table[index]
        while current is not None:
            if current.key == id_kandang:
                current.value = jumlah_ayam
                return
            current = current.next

        new_node = Node(id_kandang, jumlah_ayam)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def cari_kandang(self, id_kandang):
        index = self.hash_function(id_kandang)

        current = self.table[index]
        while current is not None:
            if current.key == id_kandang:
                return current
            current = current.next

        return None

    def hapus_kandang(self, id_kandang):
        index = self.hash_function(id_kandang)

        current = self.table[index]
        prev = None

        while current is not None:
            if current.key == id_kandang:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return True

            prev = current
            current = current.next

        return False

    def tampilkan_data(self):
        print("\nData Kandang Ayam:")
        for i in range(self.SIZE):
            print(f"Bucket {i}: ", end="")

            current = self.table[i]

            while current is not None:
                print(
                    f"[ID Kandang:{current.key}, Jumlah Ayam:{current.value}] -> ",
                    end=""
                )
                current = current.next

            print("NULL")


def main():
    peternakan = HashMapKandangAyam()

    peternakan.tambah_kandang(101, 150)
    peternakan.tambah_kandang(111, 200)
    peternakan.tambah_kandang(121, 175)
    peternakan.tambah_kandang(102, 120)

    peternakan.tampilkan_data()

    #cari
    hasil = peternakan.cari_kandang(111)

    if hasil:
        print(
            f"\nKandang ID {hasil.key} ditemukan "
            f"dengan jumlah ayam {hasil.value} ekor"
        )
    else:
        print("\nKandang tidak ditemukan")

    #hapus
    peternakan.hapus_kandang(111)

    print("\nSetelah kandang ID 111 dihapus:")
    peternakan.tampilkan_data()


if __name__ == "__main__":
    main()