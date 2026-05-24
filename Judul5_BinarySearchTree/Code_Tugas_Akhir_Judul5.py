class Buku:
    def __init__(self, nomor_buku):
        self.nomor_buku = nomor_buku
        self.left = None
        self.right = None


class BSTPerpustakaan:
    def __init__(self):
        self.root = None

    def tambah_buku_node(self, root, nomor_buku):
        if root is None:
            return Buku(nomor_buku)

        if nomor_buku < root.nomor_buku:
            root.left = self.tambah_buku_node(root.left, nomor_buku)

        elif nomor_buku > root.nomor_buku:
            root.right = self.tambah_buku_node(root.right, nomor_buku)

        return root

    def tambah_buku(self, nomor_buku):
        self.root = self.tambah_buku_node(self.root, nomor_buku)

    def cari_buku_terkecil(self, root):
        current = root

        while current is not None and current.left is not None:
            current = current.left

        return current

    def hapus_buku_node(self, root, nomor_buku):
        if root is None:
            return None

        if nomor_buku < root.nomor_buku:
            root.left = self.hapus_buku_node(root.left, nomor_buku)

        elif nomor_buku > root.nomor_buku:
            root.right = self.hapus_buku_node(root.right, nomor_buku)

        else:
            if root.left is None and root.right is None:
                return None

            elif root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            else:
                pengganti = self.cari_buku_terkecil(root.right)
                root.nomor_buku = pengganti.nomor_buku
                root.right = self.hapus_buku_node(
                    root.right,
                    pengganti.nomor_buku
                )

        return root

    def hapus_buku(self, nomor_buku):
        self.root = self.hapus_buku_node(self.root, nomor_buku)

    def tinggi_pohon(self, root):
        if root is None:
            return -1

        kiri = self.tinggi_pohon(root.left)
        kanan = self.tinggi_pohon(root.right)

        return 1 + max(kiri, kanan)

    def tampil_level_order(self, root):
        if root is None:
            print("(Data buku kosong)")
            return

        queue = []
        queue.append(root)

        while len(queue) > 0:
            current = queue.pop(0)

            print(current.nomor_buku, end=" ")

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

        print()

    def cari_successor(self, root, nomor_buku):
        current = root
        successor = None

        while current is not None:
            if nomor_buku < current.nomor_buku:
                successor = current
                current = current.left

            elif nomor_buku > current.nomor_buku:
                current = current.right

            else:
                break

        if current is None:
            return None, False

        if current.right is not None:
            successor = self.cari_buku_terkecil(current.right)

        if successor is None:
            return None, False

        return successor.nomor_buku, True

    def cari_predecessor(self, root, nomor_buku):
        current = root
        predecessor = None

        while current is not None:
            if nomor_buku > current.nomor_buku:
                predecessor = current
                current = current.right

            elif nomor_buku < current.nomor_buku:
                current = current.left

            else:
                break

        if current is None:
            return None, False

        if current.left is not None:
            temp = current.left

            while temp.right is not None:
                temp = temp.right

            predecessor = temp

        if predecessor is None:
            return None, False

        return predecessor.nomor_buku, True


def main():
    perpustakaan = BSTPerpustakaan()
    pilih = 0

    while pilih != 7:
        print("\n=== Sistem BST Perpustakaan ===")
        print("1. Tambah Buku")
        print("2. Hapus Buku")
        print("3. Tampilkan Buku (Level-order)")
        print("4. Tinggi Pohon")
        print("5. Cari Successor Buku")
        print("6. Cari Predecessor Buku")
        print("7. Keluar")

        try:
            pilih = int(input("Pilih menu: "))

        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            try:
                nomor = int(input("Masukkan nomor buku: "))
                perpustakaan.tambah_buku(nomor)

                print(f"Nomor buku {nomor} berhasil ditambahkan")

            except ValueError:
                print("Input tidak valid!")

        elif pilih == 2:
            try:
                nomor = int(input("Masukkan nomor buku yang dihapus: "))
                perpustakaan.hapus_buku(nomor)

                print(f"Nomor buku {nomor} berhasil dihapus")

            except ValueError:
                print("Input tidak valid!")

        elif pilih == 3:
            print("Data buku: ", end="")
            perpustakaan.tampil_level_order(perpustakaan.root)

        elif pilih == 4:
            print(
                f"Tinggi pohon BST: "
                f"{perpustakaan.tinggi_pohon(perpustakaan.root)}"
            )

        elif pilih == 5:
            try:
                nomor = int(input("Cari successor nomor buku: "))

                hasil, found = perpustakaan.cari_successor(
                    perpustakaan.root,
                    nomor
                )

                if found:
                    print(f"Successor buku: {hasil}")

                else:
                    print("Successor tidak ditemukan")

            except ValueError:
                print("Input tidak valid!")

        elif pilih == 6:
            try:
                nomor = int(input("Cari predecessor nomor buku: "))

                hasil, found = perpustakaan.cari_predecessor(
                    perpustakaan.root,
                    nomor
                )

                if found:
                    print(f"Predecessor buku: {hasil}")

                else:
                    print("Predecessor tidak ditemukan")

            except ValueError:
                print("Input tidak valid!")

        elif pilih == 7:
            print("Program selesai")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()