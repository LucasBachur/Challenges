import mysql.connector
  
dataBase = mysql.connector.connect(
  host = "localhost",
  user = "edu_challenge_user",
  passwd = "password",
  database = "edu_challenge_db"
)
 
cursor = dataBase.cursor()

tablaUsuario = """CREATE TABLE usuarios (
                    id_usuario INT UNSIGNED PRIMARY KEY,
                    nombre VARCHAR(255) NOT NULL,
                    apellido VARCHAR(255) NOT NULL
                  ); """

tablaCurso = """CREATE TABLE cursos (
                    id_curso INT UNSIGNED PRIMARY KEY,
                    nombre VARCHAR(255) NOT NULL,
                    cupo INT UNSIGNED NOT NULL,
                    id_docente INT UNSIGNED NOT NULL,
                    FOREIGN KEY (id_docente) REFERENCES usuarios(id_usuario)
                 ); """

tablaUsuarioCursos = """CREATE TABLE usuarios_cursos (
                          id_curso INT UNSIGNED NOT NULL,
                          id_alumno INT UNSIGNED NOT NULL,
                          FOREIGN KEY (id_curso) REFERENCES cursos(id_curso),
                          FOREIGN KEY (id_alumno) REFERENCES usuarios(id_usuario)
                        ); """

cursor.execute(tablaUsuario)
cursor.execute(tablaCurso)
cursor.execute(tablaUsuarioCursos)
  
dataBase.close()