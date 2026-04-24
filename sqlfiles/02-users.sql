USE myapp;
CREATE TABLE IF NOT EXISTS utilisateur (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO utilisateur (name, email) VALUES 
('Ton Nom 1', 'email1@example.com'),
('Ton Nom 2', 'email2@example.com'),
('Ton Nom 3', 'email3@example.com'),
('Ton Nom 4', 'email4@example.com');
