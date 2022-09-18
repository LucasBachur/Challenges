import requests
import json

def conseguir_usu_cursos():

    datos_usuarios = requests.get("http://packages.educativa.com/samples/usuarios.json")
    datos_cursos = requests.get("http://packages.educativa.com/samples/cursos.json")

    usuarios_parsed = json.loads(datos_usuarios.text)
    cursos_parsed = json.loads(datos_cursos.text)
    
    return (usuarios_parsed, cursos_parsed)