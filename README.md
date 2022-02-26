# Tugas Kecil 1 IF2211 Strategi Algoritma
> Penyelesaian _Word Search Puzzle_ dengan Algoritma _Brute Force_

## Daftar Isi
* [Deskripsi](#deskripsi)
* [Requirements](#requirements)
* [Penggunaan](#penggunaan)
* [Penulis](#penulis)

## Deskripsi
Membuat program untuk menemukan semua kata di dalam _word search puzzle_ menggunakan algoritma _Brute Force_ 

## Requirements
- Windows **(Reccomended)**
- [Java](https://www.java.com/en/download/)
- [Java Development Kit (JDK)](https://www.oracle.com/java/technologies/downloads/)

## Penggunaan
**[PENTING]** </br>
Program hanya dapat dijalankan dalam sistem operasi **Windows**. Sebagian besar console **Windows 10** tidak menyalakan dukungan ANSI escape untuk pewarnaan tulisan dalam terminal. Agar terminal **Windows 10** dapat mendukung pewarnaan tulisan, pengguna harus mengikut langkah berikut ([referensi](https://stackoverflow.com/questions/51680709/colored-text-output-in-powershell-console-using-ansi-vt100-codes)):
1. Buka **Registry Editor** (Bisa melalui `Windows StartMenu` atau menekan `Win + R` lalu menulis `regedit`)

![image](https://user-images.githubusercontent.com/73146752/150823809-bfa17783-439e-44e8-903c-8d07e382ae50.png)

2. Atur path menjadi `Computer\HKEY_CURRENT_USER\Console` lalu klik kanan area putih kemudian `New > DWORD (32-bit) Value`

![image](https://user-images.githubusercontent.com/73146752/150825618-09b0e934-a929-47b6-b331-e67f983edaae.png)

3. Ganti nama variabel yang baru dibuat menjadi `VirtualTerminalLevel`

![image](https://user-images.githubusercontent.com/73146752/150826575-22ec04ad-c3ed-464a-b81a-430b42e581fe.png)
![image](https://user-images.githubusercontent.com/73146752/150826649-8fd57ca7-8f2a-4e39-a386-fbf184ec1006.png)

4. Klik kanan `VirtualTerminalLevel` lalu pilih `Modify`, kemudian isi `Value data` menjadi 1

![image](https://user-images.githubusercontent.com/73146752/150827213-e8259d27-cf09-4449-a610-4fcf5702a05c.png)
![image](https://user-images.githubusercontent.com/73146752/150827266-b4c10e17-72c5-4fdb-8484-59e7721c2ac7.png)

### Langkah Menjalankan Program
### A. Melalui _Batch File_ / `run.bat` (**Windows**)
`run.bat` akan melakukan kompilasi program secara otomatis melalui **Command Prompt**.</br>
Jalankan `run.bat` pada folder `bin` untuk memulai program _Word Search Puzzle_

### B. Melalui **Command Prompt/Powershell** (**Windows**)
1. Atur path folder menjadi `Tucil1_13520082/bin`

![image](https://user-images.githubusercontent.com/73146752/151102124-4c058900-38bd-493e-88c1-cd77c12f22aa.png)

2. Jalankan perintah berikut untuk memulai program _Word Search Puzzle_:
```
javac -d ../bin ../src/Puzzle.java
java Puzzle
```

### Langkah Penggunaan Program
1. Jika ingin menambahkan **studi kasus**, masukkan **studi kasus** dalam folder `test` dengan ekstensi `.txt`. Contohnya `small1.txt`
2. Jalankan program melalui cara **A** atau cara **B** yang telah disinggung sebelumnya
3. Masukkan nama file tanpa mencantumkan ekstensi `.txt`. Contohnya `small1`
4. Selamat melihat program menyelesaikan _Word Search Puzzle_ :)

# Penulis
Nama: Jeremy Rionaldo Pasaribu </br>
NIM: 13520082

