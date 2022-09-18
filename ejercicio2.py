# -*- coding: utf-8 -*-
import sys

def formatear(nom):
    # [::-1] nos da vuelta el array
    nom2 = nom[::-1].split(' ', 1)
    nom3 = nom2[0][::-1] + ", " + nom2[1][::-1]
    return nom3

def ordenar(lista):
    lista2 = []
    for elem in lista:
        lista2.append(formatear(elem))
    lista3 = sorted(lista2)
    dic = {}
    for i in range(len(lista3)):
        dic[i+1] = lista3[i]
    return dic

# Uso un metodo aparte para imprimir el diccionario,
# porque el print normal nos imprime literalmente el contenido del mismo.
# O sea, no nos muestra las tildes, si no que nos muestra
# como estan representadas internamente.
def print_dic(dic):
    # Uso sys.stdout.write porque el print normal deja o bien
    # un salto de linea o un espacio al final del string a imprimir.
    sys.stdout.write("{"),
    for i in range(len(dic)):
        sys.stdout.write('{}: "{}"'.format(i+1, dic[i+1])),
        if i + 1 != len(dic) : sys.stdout.write(', '),
    sys.stdout.write("}\n")

lista_nombres = ["Jacinta Flores", "Juan Carlos Feletti", "Pedro Lugones", "Ana María Galíndez"]

lista_ord = ordenar(lista_nombres)

# print(lista_ord)
print_dic(lista_ord)