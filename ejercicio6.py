from request import conseguir_usu_cursos
from tabulate import tabulate
import mysql.connector
import sys

def mostrar_lista(db):
    cursor = db.cursor()
    query = "SELECT us_cur.id_alumno, us_cur.id_curso,\
                    us.nombre, us.apellido, cur.nombre, us2.nombre, us2.apellido \
            FROM usuarios us\
            JOIN usuarios_cursos us_cur ON us_cur.id_alumno = us.id_usuario \
            JOIN cursos cur ON cur.id_curso = us_cur.id_curso\
            JOIN usuarios us2 ON us2.id_usuario = cur.id_docente\
            ORDER BY us_cur.id_alumno"

    cursor.execute(query)

    datos = cursor.fetchall()
    
    tabla = []
    for dato in datos:
        elem = []
        for atr in dato:
            elem.append(atr)
        tabla.append(elem)

    print(tabulate(tabla, 
                   headers = ['id_usuario', 'id_curso', 'nom_usuario',
                              'ape_usuario', 'nom_curso',
                              'nom_docente', 'ape_docente'],
                   tablefmt='orgtbl'))

def inscribir(db, usuario, curso):
    cursor = db.cursor()
    query = "SELECT id_curso, id_alumno\
             FROM usuarios_cursos\
             WHERE id_curso = %s"
    cursor.execute(query, [curso])
    alumnos_curso =  cursor.fetchall()

    if ((int(curso), int(usuario)) in alumnos_curso):
        print("El usuario {} ya esta inscripto en el curso {}".format(usuario, curso))
    
    else:
        query2 = "SELECT cupo, id_docente\
                FROM cursos\
                WHERE id_curso = %s" 
        cursor.execute(query2, [curso])
        datos_curso = cursor.fetchall()[0]
        if (int(usuario) == datos_curso[1]):
            print("El usuario {} es el docente del curso {},\
 por lo que no puede inscribirse al mismo".format(usuario, curso))
        else:
            if (datos_curso[0] > len(alumnos_curso)):
                sql = "INSERT INTO usuarios_cursos (id_alumno, id_curso)\
                    VALUES (%s, %s)"
                val = [usuario, curso]
                cursor.execute(sql,val)
                db.commit()
                print("Se inscribio el usuario {} al curso {}".format(usuario, curso))
            else: print("No hay cupo disponible para el curso {}".format(curso))

def desinscribir(db, usuario, curso):
    cursor = db.cursor()
    sql = "DELETE FROM usuarios_cursos\
           WHERE id_curso = %s\
           AND id_alumno = %s"
    val = [curso, usuario]
    cursor.execute(sql, val)
    db.commit()

if(len(sys.argv) != 1 and sys.argv[1] in ["1", "2", "3"]):
    dataBase = mysql.connector.connect(
    host = "localhost",
    user = "edu_challenge_user",
    passwd = "password",
    database = "edu_challenge_db"
    )

    if sys.argv[1] == "1": 
        if len(sys.argv) ==2: mostrar_lista(dataBase)
        else: print("Faltan o sobran argumentos")

    if sys.argv[1] == "2":
        if len(sys.argv) == 4:
            inscribir(dataBase, sys.argv[2], sys.argv[3])
        else: print("Faltan o sobran argumentos")
    
    if sys.argv[1] == "3":
        if len(sys.argv) == 4:
            desinscribir(dataBase, sys.argv[2], sys.argv[3])
        else: print("Faltan o sobran argumentos")

    dataBase.close()

else:
    print("Debe indicar una de las siguientes opciones:\n\
           1) mostrar lista de inscripciones\n\
           2) inscribir usuario\n\
           3) eliminar inscripcion")


