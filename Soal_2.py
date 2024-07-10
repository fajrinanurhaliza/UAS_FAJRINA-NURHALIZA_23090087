import numpy as np

array = []
jumlah_Mahasiswa = int(input("Masukkan Jumlah Mahasiswa : "))
print(35*'=')
for i in range(jumlah_Mahasiswa):
    for i in range(jumlah_Mahasiswa):
        nilai1 = int(input(f"Masukkan Nilai Nilai Algoritma dan Struktur Data 2 Mahaiswa ke-{i+1} : "))
        nilai2 = int(input(f"Masukkan Nilai Nilai Matematika Numerik Mahaiswa ke-{i+1} : "))
        array.append(nilai1)
        array.append(nilai2)

print(35*'=')
rata_rata = np.mean(array)
print(f'Nilai Rata-Rata Setiap mata Kuliah : {rata_rata}')
print(f'Jumlah Mahaiswa Diatas Rata-Rata : {np.sum(array > rata_rata )}')