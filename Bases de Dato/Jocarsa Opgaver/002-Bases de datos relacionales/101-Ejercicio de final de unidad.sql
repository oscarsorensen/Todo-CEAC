--- Paso 1 -------------------------------------------------------------
sudo mysql -u root -p

CREATE DATABASE biblioteca25;
USE biblioteca25;
SELECT DATABASE();

--- Paso 2 -------------------------------------------------------------
-- Tabla autores sin restricciones
CREATE TABLE autores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL,
    pais VARCHAR(80) NOT NULL
);

INSERT INTO autores (name, surname, pais) VALUES
('Isabel', 'Allende', 'Chile'),
('Gabriel', 'García Márquez', 'Colombia'),
('Haruki', 'Murakami', 'Japón');

Describe autores;

mysql> Describe autores;
+---------+--------------+------+-----+---------+----------------+
| Field   | Type         | Null | Key | Default | Extra          |
+---------+--------------+------+-----+---------+----------------+
| id      | int          | NO   | PRI | NULL    | auto_increment |
| name    | varchar(100) | NO   |     | NULL    |                |
| surname | varchar(100) | NO   |     | NULL    |                |
| pais    | varchar(80)  | NO   |     | NULL    |                |
+---------+--------------+------+-----+---------+----------------+
4 rows in set (0,00 sec)

mysql> 

--- Paso 3 -------------------------------------------------------------
-- Tabla libros con restricciones, claves foráneas e índices
CREATE TABLE libros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    isbn VARCHAR(20) NOT NULL UNIQUE,
    precio DECIMAL(8,2) NOT NULL CHECK (precio >= 0),
    autor_id INT NOT NULL,
    FOREIGN KEY (autor_id) REFERENCES autores(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    INDEX (titulo)
);

INSERT INTO libros (titulo, isbn, precio, autor_id) VALUES
('La casa de los espíritus', '9788401352836', 19.99, 1),
('Cien años de soledad', '9780307474728', 17.50, 2),
('Kafka en la orilla', '9788499082478', 22.00, 3);

DESCRIBE libros;
mysql> DESCRIBE libros;
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| id       | int          | NO   | PRI | NULL    | auto_increment |
| titulo   | varchar(200) | NO   | MUL | NULL    |                |
| isbn     | varchar(20)  | NO   | UNI | NULL    |                |
| precio   | decimal(8,2) | NO   |     | NULL    |                |
| autor_id | int          | NO   | MUL | NULL    |                |
+----------+--------------+------+-----+---------+----------------+
5 rows in set (0,01 sec)

mysql> 

SHOW INDEX FROM libros;
mysql> SHOW INDEX FROM libros;
+--------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| Table  | Non_unique | Key_name | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment | Visible | Expression |
+--------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| libros |          0 | PRIMARY  |            1 | id          | A         |           3 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| libros |          0 | isbn     |            1 | isbn        | A         |           3 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| libros |          1 | autor_id |            1 | autor_id    | A         |           3 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| libros |          1 | titulo   |            1 | titulo      | A         |           3 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
+--------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
4 rows in set (0,01 sec)

mysql> 

SELECT * FROM libros;
mysql> SELECT * FROM libros;
+----+---------------------------+---------------+--------+----------+
| id | titulo                    | isbn          | precio | autor_id |
+----+---------------------------+---------------+--------+----------+
|  1 | La casa de los espíritus  | 9788401352836 |  19.99 |        1 |
|  2 | Cien años de soledad      | 9780307474728 |  17.50 |        2 |
|  3 | Kafka en la orilla        | 9788499082478 |  22.00 |        3 |
+----+---------------------------+---------------+--------+----------+
3 rows in set (0,00 sec)

mysql> 


--- Paso 4 -------------------------------------------------------------
-- Tabla socios con restricciones y valores por defecto
CREATE TABLE socios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    fecha_alta DATE NOT NULL DEFAULT (CURRENT_DATE),
    CHECK (email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$')
);

-- 2 registros válidos
INSERT INTO socios (nombre, email) VALUES ('Ana Ruiz', 'ana.ruiz@example.com');
INSERT INTO socios (nombre, email) VALUES ('Luis Pérez', 'luis.perez@example.com');
mysql> describe socios;
+------------+--------------+------+-----+-----------+-------------------+
| Field      | Type         | Null | Key | Default   | Extra             |
+------------+--------------+------+-----+-----------+-------------------+
| id         | int          | NO   | PRI | NULL      | auto_increment    |
| nombre     | varchar(100) | NO   |     | NULL      |                   |
| email      | varchar(120) | NO   | UNI | NULL      |                   |
| fecha_alta | date         | NO   |     | curdate() | DEFAULT_GENERATED |
+------------+--------------+------+-----+-----------+-------------------+
4 rows in set (0,01 sec)

mysql> 


-- 1 registro inválido (email sin '@') → produce error por CHECK
INSERT INTO socios (nombre, email) VALUES ('Marta Gómez', 'martagomez.example.com');

mysql> INSERT INTO socios (nombre, email) VALUES ('Marta Gómez', 'martagomez.example.com');
ERROR 3819 (HY000): Check constraint 'socios_chk_1' is violated.
mysql> 


--- Paso 5 -------------------------------------------------------------
-- Tabla prestamos con restricciones y valores por defecto
CREATE TABLE prestamos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    socio_id INT NOT NULL,
    libro_id INT NOT NULL,
    fecha_prestamo DATE NOT NULL DEFAULT (CURRENT_DATE),
    fecha_devolucion DATE NULL,
    CHECK (fecha_devolucion IS NULL OR fecha_devolucion >= fecha_prestamo),
    FOREIGN KEY (socio_id) REFERENCES socios(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    FOREIGN KEY (libro_id) REFERENCES libros(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    INDEX (socio_id, libro_id)
);

SHOW INDEX FROM prestamos;
mysql> SHOW INDEX FROM prestamos;
+-----------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| Table     | Non_unique | Key_name | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment | Visible | Expression |
+-----------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| prestamos |          0 | PRIMARY  |            1 | id          | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| prestamos |          1 | libro_id |            1 | libro_id    | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| prestamos |          1 | socio_id |            1 | socio_id    | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| prestamos |          1 | socio_id |            2 | libro_id    | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
+-----------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
4 rows in set (0,02 sec)

mysql> 


INSERT INTO prestamos (socio_id, libro_id) VALUES (1, 2); -- OK
INSERT INTO prestamos (socio_id, libro_id, fecha_prestamo, fecha_devolucion) VALUES (2, 1, '2024-05-15', '2024-06-15');
mysql> DESCRIBE prestamos;
+------------------+------+------+-----+-----------+-------------------+
| Field            | Type | Null | Key | Default   | Extra             |
+------------------+------+------+-----+-----------+-------------------+
| id               | int  | NO   | PRI | NULL      | auto_increment    |
| socio_id         | int  | NO   | MUL | NULL      |                   |
| libro_id         | int  | NO   | MUL | NULL      |                   |
| fecha_prestamo   | date | NO   |     | curdate() | DEFAULT_GENERATED |
| fecha_devolucion | date | YES  |     | NULL      |                   |
+------------------+------+------+-----+-----------+-------------------+
5 rows in set (0,00 sec)

mysql> 


INSERT INTO prestamos (socio_id, libro_id, fecha_devolucion) VALUES (1, 3, '2024-05-01'); -- ERROR: CHECK

mysql> INSERT INTO prestamos (socio_id, libro_id, fecha_devolucion) VALUES (1, 3, '2024-05-01'); -- ERROR: CHECK
ERROR 3819 (HY000): Check constraint 'prestamos_chk_1' is violated.
mysql> 

DESCRIBE prestamos;
mysql> DESCRIBE prestamos;
+------------------+------+------+-----+-----------+-------------------+
| Field            | Type | Null | Key | Default   | Extra             |
+------------------+------+------+-----+-----------+-------------------+
| id               | int  | NO   | PRI | NULL      | auto_increment    |
| socio_id         | int  | NO   | MUL | NULL      |                   |
| libro_id         | int  | NO   | MUL | NULL      |                   |
| fecha_prestamo   | date | NO   |     | curdate() | DEFAULT_GENERATED |
| fecha_devolucion | date | YES  |     | NULL      |                   |
+------------------+------+------+-----+-----------+-------------------+
5 rows in set (0,00 sec)

mysql> 

SHOW INDEX FROM prestamos;
mysql> SHOW INDEX FROM prestamos;
+-----------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| Table     | Non_unique | Key_name | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment | Visible | Expression |
+-----------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| prestamos |          0 | PRIMARY  |            1 | id          | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| prestamos |          1 | libro_id |            1 | libro_id    | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| prestamos |          1 | socio_id |            1 | socio_id    | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| prestamos |          1 | socio_id |            2 | libro_id    | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
+-----------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
4 rows in set (0,00 sec)

mysql> 


--- Paso 6 -------------------------------------------------------------
SELECT * FROM autores;
mysql> SELECT * FROM autores;
+----+---------+------------------+----------+
| id | name    | surname          | pais     |
+----+---------+------------------+----------+
|  1 | Isabel  | Allende          | Chile    |
|  2 | Gabriel | García Márquez   | Colombia |
|  3 | Haruki  | Murakami         | Japón    |
+----+---------+------------------+----------+
3 rows in set (0,00 sec)

mysql> 

SELECT * FROM libros;
mysql> SELECT * FROM libros;
+----+---------------------------+---------------+--------+----------+
| id | titulo                    | isbn          | precio | autor_id |
+----+---------------------------+---------------+--------+----------+
|  1 | La casa de los espíritus  | 9788401352836 |  19.99 |        1 |
|  2 | Cien años de soledad      | 9780307474728 |  17.50 |        2 |
|  3 | Kafka en la orilla        | 9788499082478 |  22.00 |        3 |
+----+---------------------------+---------------+--------+----------+
3 rows in set (0,01 sec)

mysql> 

SELECT * FROM socios;
mysql> SELECT * FROM socios;
+----+-------------+------------------------+------------+
| id | nombre      | email                  | fecha_alta |
+----+-------------+------------------------+------------+
|  1 | Ana Ruiz    | ana.ruiz@example.com   | 2025-10-31 |
|  2 | Luis Pérez  | luis.perez@example.com | 2025-10-31 |
+----+-------------+------------------------+------------+
2 rows in set (0,00 sec)

mysql> 

SELECT * FROM prestamos;
mysql> SELECT * FROM prestamos;
+----+----------+----------+----------------+------------------+
| id | socio_id | libro_id | fecha_prestamo | fecha_devolucion |
+----+----------+----------+----------------+------------------+
|  1 |        1 |        2 | 2025-10-31     | NULL             |
|  2 |        2 |        1 | 2024-05-15     | 2024-06-15       |
+----+----------+----------+----------------+------------------+
2 rows in set (0,00 sec)

mysql> 


--- Paso final ---------------------------------------------------------
SHOW TABLES;
mysql> SHOW TABLES;
+------------------------+
| Tables_in_biblioteca25 |
+------------------------+
| autores                |
| libros                 |
| prestamos              |
| socios                 |
+------------------------+
4 rows in set (0,00 sec)


DESCRIBE autores;
mysql> DESCRIBE autores;
+---------+--------------+------+-----+---------+----------------+
| Field   | Type         | Null | Key | Default | Extra          |
+---------+--------------+------+-----+---------+----------------+
| id      | int          | NO   | PRI | NULL    | auto_increment |
| name    | varchar(100) | NO   |     | NULL    |                |
| surname | varchar(100) | NO   |     | NULL    |                |
| pais    | varchar(80)  | NO   |     | NULL    |                |
+---------+--------------+------+-----+---------+----------------+
4 rows in set (0,00 sec)

mysql> 

DESCRIBE libros;
mysql> DESCRIBE libros;
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| id       | int          | NO   | PRI | NULL    | auto_increment |
| titulo   | varchar(200) | NO   | MUL | NULL    |                |
| isbn     | varchar(20)  | NO   | UNI | NULL    |                |
| precio   | decimal(8,2) | NO   |     | NULL    |                |
| autor_id | int          | NO   | MUL | NULL    |                |
+----------+--------------+------+-----+---------+----------------+
5 rows in set (0,00 sec)


DESCRIBE socios;

mysql> DESCRIBE socios;
+------------+--------------+------+-----+-----------+-------------------+
| Field      | Type         | Null | Key | Default   | Extra             |
+------------+--------------+------+-----+-----------+-------------------+
| id         | int          | NO   | PRI | NULL      | auto_increment    |
| nombre     | varchar(100) | NO   |     | NULL      |                   |
| email      | varchar(120) | NO   | UNI | NULL      |                   |
| fecha_alta | date         | NO   |     | curdate() | DEFAULT_GENERATED |
+------------+--------------+------+-----+-----------+-------------------+
4 rows in set (0,00 sec)

mysql> 
