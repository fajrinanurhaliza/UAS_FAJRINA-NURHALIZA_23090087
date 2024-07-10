def main():
    Mahasiswa = {}

    while True:
        NIM = str(input("Masukkan NIM: "))
        Nama = str(input("Masukkan Nama "))
        
        Mahasiswa[NIM] = Nama
        
        Tambah = str(input("ingin menambahkan Data lagi? (ya/tidak): ").strip().lower())
        if Tambah != 'ya':
            break
    
    print("\nData Mahasiswa:")
    for NIM, Nama in Mahasiswa.items():
        print(f"NIM: {NIM}, Nama: {Nama}")
    
    print("\nSelesai.")

if __name__ == "__main__":
    main()