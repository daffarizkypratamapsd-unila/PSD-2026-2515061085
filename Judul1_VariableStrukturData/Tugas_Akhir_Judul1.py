def menu():
    print("\n=== MENU ===")
    print("1. Masukkan nilai kedalam semua index array")
    print("2. Tampilkan data nilai siswa")
    print("3. Analisis nilai (rata-rata, max, min)")
    print("4. Keluar")


def main():
    a = [0] * 5
    running = True

    while running:
        menu()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        if choice == 1:
            print("Masukkan 5 nilai siswa:")
            for i in range(5):
                while True:
                    try:
                        a[i] = int(input(f"Nilai siswa ke-{i+1}: "))
                        break
                    except ValueError:
                        print("Input tidak valid, masukkan angka!")

            print(f"Data nilai sekarang: {a}")

        elif choice == 2:
            print("\n=== DATA NILAI SISWA ===")
            for i in range(5):
                print(f"Siswa ke-{i+1}: {a[i]}")

        elif choice == 3:
            print("\n=== ANALISIS NILAI ===")
            total = sum(a)
            rata = total / len(a)
            maksimum = max(a)
            minimum = min(a)

            print(f"Total nilai    : {total}")
            print(f"Rata-rata      : {rata}")
            print(f"Nilai tertinggi: {maksimum}")
            print(f"Nilai terendah : {minimum}")

        elif choice == 4:
            running = False
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
