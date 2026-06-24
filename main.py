"""
Menu interactivo de consola para el Sistema de Gestion de Biblioteca.

Este archivo NO modifica ninguna clase: solo USA las clases Biblioteca y Libro
que estan en sistema.py. Separar el menu (interfaz) de las clases (logica) es
una buena practica de diseno.
"""
from sistema import Biblioteca, Libro


def mostrar_menu():
    print("\n" + "=" * 42)
    print("     SISTEMA DE GESTION DE BIBLIOTECA")
    print("=" * 42)
    print(" 1. Agregar libro")
    print(" 2. Ver catalogo completo")
    print(" 3. Buscar libro")
    print(" 4. Ver libros disponibles")
    print(" 5. Prestar libro")
    print(" 6. Devolver libro")
    print(" 0. Salir")
    print("=" * 42)


def opcion_agregar(biblio):
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    genero = input("Genero: ")
    editorial = input("Editorial: ")
    biblio.agregar_libro(Libro(titulo, autor, genero, editorial))
    print(f"-> Libro '{titulo}' agregado.")


def opcion_catalogo(biblio):
    libros = biblio.catalogo()
    if not libros:
        print("-> La biblioteca esta vacia.")
        return
    print("Catalogo:")
    for libro in libros:
        print("   ", libro)


def opcion_buscar(biblio):
    titulo = input("Titulo a buscar: ")
    libro = biblio.buscar_libro(titulo)
    if libro is None:
        print("-> No se encontro ese libro.")
    else:
        print("-> Encontrado:", libro)


def opcion_disponibles(biblio):
    disponibles = biblio.libros_disponibles()
    print(f"Disponibles ({biblio.cantidad_disponible()}):")
    if not disponibles:
        print("   (ninguno)")
    for libro in disponibles:
        print("   ", libro)


def opcion_prestar(biblio):
    titulo = input("Titulo a prestar: ")
    libro = biblio.buscar_libro(titulo)
    if libro is None:
        print("-> No existe ese libro.")
    elif libro.esta_prestado():
        print("-> Ese libro ya esta prestado.")
    else:
        libro.prestar()
        print(f"-> '{titulo}' prestado con exito.")
    # NOTA: cuando la clase Prestamo este lista, se puede reemplazar lo de
    # arriba por:   print(biblio.registrar_prestamo(usuario, titulo))
    # para que ademas quede registrado el objeto Prestamo.


def opcion_devolver(biblio):
    titulo = input("Titulo a devolver: ")
    print("->", biblio.registrar_devolucion(titulo))


def main():
    biblio = Biblioteca()
    # Diccionario que asocia cada opcion con su funcion (despacho limpio,
    # mas prolijo que un if/elif gigante).
    opciones = {
        "1": opcion_agregar,
        "2": opcion_catalogo,
        "3": opcion_buscar,
        "4": opcion_disponibles,
        "5": opcion_prestar,
        "6": opcion_devolver,
    }

    while True:
        mostrar_menu()
        eleccion = input("Elegi una opcion: ").strip()
        if eleccion == "0":
            print("Hasta luego!")
            break
        accion = opciones.get(eleccion)
        if accion:
            accion(biblio)
        else:
            print("-> Opcion invalida, intenta de nuevo.")


if __name__ == "__main__":
    main()