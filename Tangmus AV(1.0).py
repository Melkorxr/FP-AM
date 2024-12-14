import os
import hashlib
import logging
import mysql.connector
import tkinter as tk
from tkinter import filedialog, messagebox

# Logging untuk mencatat aktivitas
logging.basicConfig(
    filename="antivirus.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
# Mengambil signature malware dari database MySQL.
def get_malware_signatures():
    signatures = {}
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="av",  # Ganti dengan username MySQL Anda
            password="DAMAR01",  # Ganti dengan password MySQL Anda
            database="antivirus_db",
            charset="utf8mb4",
            collation="utf8mb4_general_ci"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT md5_hash, malware_name FROM malware_signatures")
        for md5_hash, malware_name in cursor.fetchall():
            signatures[md5_hash] = malware_name
    except mysql.connector.Error as err:
        logging.error(f"Database error: {err}")
        print(f"[ERROR] Could not retrieve malware signatures: {err}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
    return signatures

 # Menghitung MD5 hash dari sebuah file.
def calculate_md5(file_path):
    try:
        with open(file_path, 'rb') as file:
            hasher = hashlib.md5()
            while chunk := file.read(4096):
                hasher.update(chunk)
            return hasher.hexdigest()
    except Exception as e:
        logging.error(f"Error hashing file {file_path}: {e}")
        return None

# Memindai file untuk mendeteksi malware dan menghapus jika ditemukan.
def scan_file(file_path, malware_signatures, text_widget):
    md5_hash = calculate_md5(file_path)
    if md5_hash is None:
        return False

    if md5_hash in malware_signatures:
        malware_name = malware_signatures[md5_hash]
        logging.warning(f"MALWARE DETECTED: {file_path} - {malware_name}")
        message = f"MALWARE DETECTED: {file_path} - {malware_name}\n"
        text_widget.insert(tk.END, message)
        text_widget.see(tk.END)
        delete_file(file_path, text_widget)
        return True

    logging.info(f"File scanned: {file_path} - No malware detected.")
    text_widget.insert(tk.END, f"[SAFE] {file_path} - No malware detected.\n")
    text_widget.see(tk.END)
    return False

 # Memindai semua file dalam direktori dan subdirektori.
def scan_directory(directory, text_widget):
    if not os.path.isdir(directory):
        messagebox.showerror("Error", f"{directory} is not a valid directory.")
        return

    malware_signatures = get_malware_signatures()
    text_widget.insert(tk.END, f"Scanning directory: {directory}\n")
    text_widget.see(tk.END)
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            scan_file(file_path, malware_signatures, text_widget)

# Menghapus file yang terdeteksi sebagai malware.
def delete_file(file_path, text_widget):
    try:
        os.remove(file_path)
        logging.info(f"File deleted: {file_path}")
        text_widget.insert(tk.END, f"[DELETED] {file_path}\n")
        text_widget.see(tk.END)
    except Exception as e:
        logging.error(f"Error deleting file {file_path}: {e}")
        text_widget.insert(tk.END, f"[ERROR] Failed to delete {file_path}\n")
        text_widget.see(tk.END)

# Membuka dialog untuk memilih direktori.
def browse_directory(text_widget):
    directory = filedialog.askdirectory()
    if directory:
        scan_directory(directory, text_widget)

# Membuat antarmuka GUI untuk antivirus.
def create_gui():
    window = tk.Tk()
    window.title("Tangmus AV")

    # Label
    label = tk.Label(window, text="Select a directory to scan for malware:")
    label.pack(pady=10)

    # Tombol untuk memilih direktori
    browse_button = tk.Button(window, text="Browse", command=lambda: browse_directory(text_widget))
    browse_button.pack(pady=5)

    # Text widget untuk menampilkan hasil pemindaian
    text_widget = tk.Text(window, width=80, height=20, wrap=tk.WORD)
    text_widget.pack(padx=10, pady=10)

    # Mulai aplikasi
    window.mainloop()


if __name__ == "__main__":
    create_gui()
