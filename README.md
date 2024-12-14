# TANGMUS AV

TANGMUS AV adalah sebuah aplikasi antivirus berbasis Python yang dirancang untuk membantu pengguna memindai dan menghapus malware dari komputer. Aplikasi ini memanfaatkan tanda tangan (signature) malware yang disimpan dalam database MySQL untuk deteksi yang efektif.

---

## Fitur
- Pemindaian file dan direktori secara manual.
- Deteksi malware berdasarkan hash MD5 menggunakan database MySQL.
- Penghapusan otomatis file yang terdeteksi sebagai malware.
- Antarmuka grafis pengguna (GUI) menggunakan Tkinter.

---

## Riwayat Versi
### TANGMUS 1.0
- Menambahkan antarmuka grafis pengguna (GUI) menggunakan Tkinter.

### TANGMUS 0.8
- File yang terindikasi sebagai malware langsung dihapus daripada dipindahkan ke folder khusus.

### TANGMUS 0.6
- Menambahkan integrasi database MySQL untuk menyimpan lebih banyak hash malware.

### TANGMUS 0.4
- File yang terindikasi malware dipindahkan ke folder karantina khusus.

### TANGMUS 0.2
- Implementasi pemindaian manual pada direktori dan file.
- Memberikan peringatan terkait file yang terdeteksi sebagai malware.

---

## Instalasi
Ikuti langkah-langkah berikut untuk menginstal dan menjalankan aplikasi ini:

1. **Buat Virtual Environment**:
   ```bash
   python3 -m venv av
   source av/bin/activate
2. **Instalasi Depedensi**:
   ```bash
   pip install mysql-connector-python
   pip freeze > requirements.txt
3. **Tambahan untuk Kali Linux**:
   ```bash
   sudo apt-get install python3-tk

---

## Lisensi

Dilisensikan di bawah [Lisensi MIT](LICENSE).

Copyright © 2024 MelkorXR

Dengan ini diizinkan untuk siapa saja yang memperoleh salinan perangkat lunak ini dan file dokumentasi terkait ("Perangkat Lunak") untuk menggunakan Perangkat Lunak tanpa batasan, termasuk tanpa batasan hak untuk menggunakan, menyalin, memodifikasi, menggabungkan, menerbitkan, mendistribusikan, melisensikan ulang, dan/atau menjual salinan Perangkat Lunak, serta memberikan izin kepada orang-orang yang menerima Perangkat Lunak untuk melakukan hal yang sama, dengan ketentuan berikut:

Salinan pemberitahuan hak cipta di atas dan pemberitahuan izin ini harus disertakan dalam semua salinan atau bagian substansial dari Perangkat Lunak.

PERANGKAT LUNAK INI DISEDIAKAN "APA ADANYA", TANPA JAMINAN DALAM BENTUK APA PUN, BAIK TERSURAT MAUPUN TERSIRAT, TERMASUK NAMUN TIDAK TERBATAS PADA JAMINAN DIPERDAGANGKAN, KESESUAIAN UNTUK TUJUAN TERTENTU DAN KEBEBASAN DARI PELANGGARAN. DALAM HAL APA PUN PENULIS ATAU PEMEGANG HAK CIPTA TIDAK BERTANGGUNG JAWAB ATAS KLAIM, KERUSAKAN, ATAU KEWAJIBAN LAINNYA, BAIK DALAM TINDAKAN KONTRAK, KERUGIAN ATAU SEBAGAINYA, YANG TIMBUL DARI, DARI ATAU DALAM HUBUNGAN DENGAN PERANGKAT LUNAK ATAU PENGGUNAAN ATAU TRANSAKSI LAIN DALAM PERANGKAT LUNAK.

