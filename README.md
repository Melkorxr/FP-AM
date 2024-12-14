# FP-AM

TANGMUS AV 
---------------
Sebuah aplikasi antivirus dengan bahasa pemrograman python. TANGMUS AV dibuat untuk membantu pengguna memindai dan menghapus malware 
di komputer mereka dengan memanfaatkan tanda tangan (signature) dari malware yang terdaftar dalam database MySQL.

=====================================================================================================================================

Riwayat Versi -
--------------------
TANGMUS 1.0
Menambahkan Interface GUI.

TANGMUS 0.8
Menghapus langsung file yang terindikasi malware daripada memindahkannya ke folder khusus.

TANGMUS 0.6
Menggabungkan database mysql untuk menyimpan lebih banyak kode hash malware.

TANGMUS 0.4
Memindahkan file yang terindikasi Malware ke folder khusus.

TANGMUS 0.2
Melakukan Scanning manual pada direktori dan File.
Memberikan peringatan terkait file yang terindikasi Malware.

==================================================================================================

Instalasi Tambahan -
------------------------

1. python3 -m venv av
2. source av/bin/activate
3. pip install mysql-connector-python
4. pip freeze > requirements.txt
5. sudo apt-get install python3-tk (for kali-linux)
========================================================



Copyright @MelkorXR
===========================
