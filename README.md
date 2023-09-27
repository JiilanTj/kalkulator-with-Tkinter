# Kalkulator Sederhana dengan Tkinter

Kode ini adalah implementasi kalkulator sederhana yang menggunakan library Tkinter untuk membangun antarmuka pengguna. Kalkulator ini dapat melakukan operasi matematika dasar seperti penjumlahan, pengurangan, perkalian, dan pembagian. Berikut adalah penjelasan singkat tentang bagaimana kode ini berfungsi:

1. `on_click(event)`: Ini adalah fungsi yang akan dipanggil ketika salah satu tombol pada kalkulator ditekan. Fungsi ini mengambil teks dari tombol yang ditekan dan menentukan tindakan yang harus diambil. Jika tombol "=" ditekan, fungsi akan mencoba menghitung hasil dari ekspresi matematika yang ada di dalam `entry` (kotak teks) menggunakan fungsi `eval()`. Hasil perhitungan akan ditampilkan kembali di `entry`. Jika terjadi kesalahan dalam perhitungan, pesan "Error" akan ditampilkan. Jika tombol "C" ditekan, isi `entry` akan dihapus. Untuk tombol lainnya, teks dari tombol tersebut akan ditambahkan ke dalam `entry`.

2. Membuat jendela utama menggunakan `tk.Tk()` dan mengatur judul jendela.

3. Membuat `entry` untuk memasukkan ekspresi matematika. `entry` akan digunakan untuk menampilkan ekspresi dan hasil perhitungan.

4. Membuat tombol-tombol kalkulator menggunakan loop `for`. Setiap tombol akan memiliki teks yang sesuai dan akan terhubung ke fungsi `on_click()` menggunakan metode `bind()`. Tombol-tombol ini akan ditempatkan di jendela kalkulator sesuai dengan tata letak matriks yang telah ditentukan.

## Menjalankan Kode

Anda dapat menjalankan kode ini dengan menggunakan interpreter Python yang sudah memiliki library Tkinter terinstal. Tkinter adalah library standar Python, jadi Anda tidak perlu menginstalnya secara terpisah.

1. Salin kode di atas dan simpan dalam sebuah file dengan ekstensi `.py`.

2. Jalankan file tersebut dengan perintah berikut melalui terminal:

   ```bash
   python nama_file.py
   ```

   Gantilah `nama_file.py` dengan nama file tempat Anda menyimpan kode ini.

## Hasil

Setelah kode dijalankan, jendela aplikasi kalkulator akan muncul. Anda dapat mengklik tombol angka, tombol operasi matematika, tombol "C" untuk menghapus, dan tombol "=" untuk menghitung hasil perhitungan. Hasil perhitungan akan ditampilkan di kotak teks (`entry`) yang ada di kalkulator.

Selamat mencoba menggunakan kalkulator sederhana ini!
