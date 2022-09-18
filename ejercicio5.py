from request import conseguir_usu_cursos
from tabulate import tabulate
import mysql.connector

(usuarios, cursos) = conseguir_usu_cursos()

dataBase = mysql.connector.connect(
  host = "localhost",
  user = "edu_challenge_user",
  passwd = "password",
  database = "edu_challenge_db"
)

cursor = dataBase.cursor()

sql1 = "INSERT INTO usuarios (id_usuario, nombre, apellido)\
        VALUES (%s, %s, %s)"

val1 = []
for usuario in usuarios['usuarios']:
    val1.append((usuario['id'], usuario['nombre'], usuario['apellido']))

sql2 = "INSERT INTO cursos (id_curso, nombre, cupo, id_docente)\
        VALUES (%s, %s, %s, %s)"

val2 = []
for curso in cursos['cursos']:
    val2.append((curso['id'], curso['nombre'], curso['cupo'], curso['id_docente']))

sql3 = "INSERT INTO usuarios_cursos (id_alumno, id_curso)\
        VALUES (%s, %s)"

val3 = []
for usuario in usuarios['usuarios']:
    for curso in usuario['id_curso']:
        val3.append((usuario['id'], curso))


cursor.executemany(sql1, val1)
cursor.executemany(sql2, val2)
cursor.executemany(sql3, val3)

# Si se quiere probar los datos sin necesidad de tener que agregarlos
# a la BD, se puede comentar la siguiente linea del codigo.

dataBase.commit()


query = "SELECT id_alumno, cursos.id_curso, usuarios.nombre, usuarios.apellido, cursos.nombre\
            FROM usuarios_cursos\
            JOIN usuarios ON usuarios.id_usuario = usuarios_cursos.id_alumno\
            JOIN cursos ON cursos.id_curso = usuarios_cursos.id_curso\
            ORDER BY usuarios_cursos.id_alumno"

cursor.execute(query)

datos = cursor.fetchall()

tabla = []
for dato in datos:
    elem = [dato[0], dato[1], dato[2] + dato[3], dato[4]]
    tabla.append(elem)

print(tabulate(tabla,
               headers = ['id_usuario', 'id_curso', 'nombre y apellido usuario', 'nombre curso'],
               tablefmt='orgtbl'))

dataBase.close()

