import os
import hashlib
import logging

# Database signature malware sederhana (MD5 hash contoh malware)
MALWARE_SIGNATURES = {
    "44d88612fea8a8f36de82e1278abb02f": "EICAR Test File",
    "098f6bcd4621d373cade4e832627b4f6": "Example Malware",
}

# Logging untuk mencatat aktivitas
logging.basicConfig(
    filename="antivirus.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

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

def scan_file(file_path):
    """Memindai file untuk mendeteksi malware."""
    md5_hash = calculate_md5(file_path)
    if md5_hash is None:
        return False

    if md5_hash in MALWARE_SIGNATURES:
        malware_name = MALWARE_SIGNATURES[md5_hash]
        logging.warning(f"MALWARE DETECTED: {file_path} - {malware_name}")
        print(f"[ALERT] Malware detected: {file_path} ({malware_name})")
        return True

    logging.info(f"File scanned: {file_path} - No malware detected.")
    print(f"[SAFE] {file_path} - No malware detected.")
    return False

def scan_directory(directory):
    """Memindai semua file dalam direktori dan subdirektori."""
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return

    print(f"Scanning directory: {directory}")
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            scan_file(file_path)

if __name__ == "__main__":
    # Direktori target untuk pemindaian
    target_directory = input("Enter the directory to scan: ")

    # Memindai direktori
    scan_directory(target_directory)
