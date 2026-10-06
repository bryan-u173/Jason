CREATE DATABASE IF NOT EXISTS mi_base_datos CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'usuario_django'@'localhost' IDENTIFIED BY 'personasdecolorenparis';

GRANT ALL PRIVILEGES ON mi_base_datos.* TO 'usuario_django'@'localhost';

FLUSH PRIVILEGES;
