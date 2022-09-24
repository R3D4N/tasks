import sqlite3


def main():

    while True:
        print("""Opciones:
        1. Insertar datos de un alumno.
        2. Buscar un alumno por su nombre.
        3. Salir.""")
        opc=int(input("Digite el numero de la opcion: "))
        match opc:
            case 1:
                nombre=input("Digite el nombre: ")
                apellido=input("Digite el apellido: ")
                insertarDatos(nombre,apellido)
            case 2:
                nombre=input("Digite el nombre a buscar: ")
                buscarAlumno(nombre)

            case 3:
                break          


def insertarDatos(nombre,apellido):
    #cambiar por el nombre o direccion de la bd
    conn=sqlite3.connect(r'.\tema11\ejercicio1\escuela.db')
    cursor=conn.cursor()
    id=obtenerID()
    query="insert into alumnos values(?,?,?)"
    cursor.execute(query,(id+1,nombre,apellido))
    conn.commit()
    cursor.close()
    conn.close()

def obtenerID():
    """obtendra el ultimo valor del ID ingresado, para ya no ingresarlo manualmente."""
    #cambiar por el nombre o direccion de la bd
    conn=sqlite3.connect(r'.\tema11\ejercicio1\escuela.db')
    cursor=conn.cursor()
    query="select max(id) from alumnos"
    rows=cursor.execute(query)
    data=rows.fetchone()
    cursor.close()
    conn.close()
    if data[0]==None:
        return 0
    else:
        return data[0]

def buscarAlumno(nombre):
    #cambiar por el nombre o direccion de la bd
    conn=sqlite3.connect(r'.\tema11\ejercicio1\escuela.db')
    cursor=conn.cursor()
    query=f"select * from alumnos where nombre=?"
    rows=cursor.execute(query,(nombre,))
    data=rows.fetchone()
    print(data)
    cursor.close()
    conn.close()

if __name__=='__main__':
    main()