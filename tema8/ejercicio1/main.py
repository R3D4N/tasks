def escribir(fichero,modo,msj):
    stream=open(fichero,modo)
    stream.writelines(msj)
    stream.close()

def main():
    fichero="newFile.txt"
    modo="at"
    mensajes=["primera linea\n","segunda linea\n"]

    for msj in mensajes:
        escribir(fichero,modo,msj)

if __name__=="__main__":
    main()