def crearFila(ancho):
    
    return ("*"*ancho)+"\n"

def crearRectangulo(ancho,alto):
   
    fila=crearFila(ancho)
    rect=fila*alto
    rta= "{}".format(rect)
    return rta
    


def main():
    ancho=int(input("Ingrese ancho: "))
    alto=int(input("Ingrese alto: "))
    print(crearRectangulo(ancho,alto))
    
main()
