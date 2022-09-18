from request import conseguir_usu_cursos

# Hago el metodo en un archivo aparte para luego poder utilizarlo
# en otro ejercicios sin que moleste el print que hay que hacer en este.

(usuarios, cursos) = conseguir_usu_cursos()

print("Usuarios:")
for usuario in usuarios["usuarios"]:
    print(usuario)

print("\nCursos:")
for curso in cursos["cursos"]:
    print(curso)
