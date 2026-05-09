def sequential_search_sentinel(data_barang, n, target):
    data_barang.append(target)
    i = 0
    while data_barang[i] != target:
        i += 1
    data_barang.pop()
    if i < n:
        return True, i
    else:
        return False, -1


def main():
    data_barang = [103, 108, 101, 109, 100, 106, 107, 105, 112, 102]

    n = len(data_barang)
    
    print(f"Daftar nomor barang: {data_barang}")

    while True:
        try:
            target = int(input("Masukkan nomor barang yang ingin dicari: "))
            break
        except ValueError:
            print("Input tidak valid! Masukkan angka.")

    found, index = sequential_search_sentinel(data_barang, n, target)

    if found:
        print(f"Barang nomor {target} ditemukan pada posisi indeks ke-{index}")
    else:
        print(f"Barang nomor {target} tidak ditemukan dalam gudang")


if __name__ == "__main__":
    main()