import os
import hashlib
import logging
import mysql.connector

# Logging untuk mencatat aktivitas
logging.basicConfig(
    filename="antivirus.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_malware_signatures():
    """Mengambil signature malware dari database MySQL."""
    signatures = {}
    connection = None  # Pastikan connection terdefinisi
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
        if connection and connection.is_connected():  # Pastikan connection ada dan aktif
            cursor.close()
            connection.close()
    return signatures


def calculate_md5(file_path):
    """Menghitung MD5 hash dari sebuah file."""
    try:
        with open(file_path, 'rb') as file:
            hasher = hashlib.md5()
            while chunk := file.read(4096):
                hasher.update(chunk)
            return hasher.hexdigest()
    except Exception as e:
        logging.error(f"Error hashing file {file_path}: {e}")
        return None

def scan_file(file_path, malware_signatures):
    """Memindai file untuk mendeteksi malware dan menghapus jika ditemukan."""
    md5_hash = calculate_md5(file_path)
    if md5_hash is None:
        return False

    if md5_hash in malware_signatures:
        malware_name = malware_signatures[md5_hash]
        logging.warning(f"MALWARE DETECTED: {file_path} - {malware_name}")
        print(f"[ALERT] Malware detected: {file_path} ({malware_name})")
        delete_file(file_path)
        return True

    logging.info(f"File scanned: {file_path} - No malware detected.")
    print(f"[SAFE] {file_path} - No malware detected.")
    return False

def scan_directory(directory):
    """Memindai semua file dalam direktori dan subdirektori."""
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return

    malware_signatures = get_malware_signatures()
    print(f"Scanning directory: {directory}")
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            scan_file(file_path, malware_signatures)

def delete_file(file_path):
    """Menghapus file yang terdeteksi sebagai malware."""
    try:
        os.remove(file_path)
        logging.info(f"File deleted: {file_path}")
        print(f"[DELETED] {file_path}")
    except Exception as e:
        logging.error(f"Error deleting file {file_path}: {e}")
        print(f"[ERROR] Failed to delete {file_path}")

if __name__ == "__main__":
    # Direktori target untuk pemindaian
    target_directory = input("Enter the directory to scan: ")

    # Memindai direktori
    scan_directory(target_directory)
