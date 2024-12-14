CREATE DATABASE IF NOT EXISTS antivirus_db CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE antivirus_db;

CREATE TABLE malware_signatures (
    md5_hash VARCHAR(32) PRIMARY KEY,
    malware_name VARCHAR(255) NOT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

INSERT INTO malware_signatures (md5_hash, malware_name) VALUES
('44d88612fea8a8f36de82e1278abb02f', 'EICAR Test File'),
('098f6bcd4621d373cade4e832627b4f6', 'Example Malware')
('fbbdc39af1139aebba4da004475e8839', 'Bad Rabbit'),
('515198a8dfa7825f746d5921a4bc4db9', 'WindowsUpdate'),
('b2eca909a91e1946457a0b36eaf90930', 'Hydra'),
('2f8f6e90ca211d7ef5f6cf3c995a40e7', 'Dekstop Puzzle');

CREATE USER 'av'@'localhost' IDENTIFIED BY 'DAMAR01';
GRANT ALL PRIVILEGES ON antivirus_db.* TO 'av'@'localhost';
FLUSH PRIVILEGES;