
-- empezar mysql en terminal
sudo mysql -u root -p;

show databases;
-- Crear base de datos PortafolioDB
CREATE DATABASE PortafolioDB;

USE PortafolioDB;

-- Crear tablas Categoria y Pieza con claves primarias
CREATE TABLE IF NOT EXISTS Categoria (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    descripcion TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Pieza (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    descripcion TEXT NOT NULL,
    imagen VARCHAR(255) NOT NULL,
    categoria_id INT NOT NULL,
    FOREIGN KEY (categoria_id) REFERENCES Categoria(id) 
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    url VARCHAR(255) NOT NULL
);

-- Hacer un LEFT JOIN entre Pieza y Categoria
SELECT 
    Pieza.id AS pieza_id,
    Pieza.titulo AS pieza_titulo,
    Categoria.titulo AS categoria_titulo
FROM Pieza
LEFT JOIN Categoria
ON Pieza.categoria_id = Categoria.id;

-- Crear una vista llamada pieza_con_categoria

CREATE OR REPLACE VIEW pieza_con_categoria AS
SELECT 
    Pieza.titulo,
    Pieza.descripcion,
    Categoria.titulo AS categoria_titulo
FROM Pieza
LEFT JOIN Categoria
ON Pieza.categoria_id = Categoria.id;

-- testear la vista

use PortafolioDB;
SELECT database();

-- Ver las vistas creadas

SHOW FULL TABLES WHERE TABLE_TYPE = 'VIEW';
