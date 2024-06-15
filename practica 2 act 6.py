import random

def peticion(cosa):
    print(cosa,end="")
    objeto=str(input())
    return objeto

def azar(cosa1,cosa2):
    decision=random.randint(0,1)
    return decision   
    
def main():
    altVes1=peticion("Ingrese alternativa 1 vestimenta: ")
    altVes2=peticion("Ingrese alternativa 2 vestimenta: ")
    altPlato1=peticion("Ingrese alternativa 1 plato: ")
    altPlato2=peticion("Ingrese alternativa 2 plato: ")
    altBeb1=peticion("Ingrese alternativa 1 bebida: ")
    altBeb2=peticion("Ingrese alternativa 2 bebida: ")
    vestimenta=altVes1*azar(0,1)+altVes2*azar(0,1)+1
    plato=altPlato1*azar(0,1)+altPlato2*azar(0,1)+1
    bebida=altBeb1*azar(0,1)+altBeb2*azar(0,1)+1
    print("Cena al azar {}, {} y {}".format(vestimenta,plato,bebida))
                                            
    
    
main()
                                        