-- Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS aire_rest;
USE aire_rest;

-- Crear tabla de alumnos (students)
CREATE TABLE IF NOT EXISTS students (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL
);

-- Crear tabla de idiomas (languages)
CREATE TABLE IF NOT EXISTS languages (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);

-- Crear tabla de unión (student_languages)
CREATE TABLE IF NOT EXISTS student_languages (
  student_id INT,
  language_id INT,
  PRIMARY KEY (student_id, language_id),
  FOREIGN KEY (student_id) REFERENCES students(id),
  FOREIGN KEY (language_id) REFERENCES languages(id)
);


