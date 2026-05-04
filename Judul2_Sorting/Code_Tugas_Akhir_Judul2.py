def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j][1] < arr[j + 1][1]:
                tukar(arr, j, j + 1)


def main():
    try:
        n = int(input("Masukkan jumlah pohon sawit: "))
    except ValueError:
        print("Input tidak valid!")
        return

    arr = []
    print("Masukkan tinggi pohon (dalam meter):")

    for i in range(n):
        while True:
            try:
                tinggi = int(input(f"Pohon ke-{i+1}: "))
                arr.append((i + 1, tinggi))
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan angka!")

    print("\nData sebelum diurutkan:")
    print(arr)

    bubble_sort(arr, n)

    print("\nHasil pengurutan tinggi pohon (tertinggi ke terendah):")
    for nomor, tinggi in arr:
        print(f"Pohon ke-{nomor} ({tinggi}m)")


if __name__ == "__main__":
    main()