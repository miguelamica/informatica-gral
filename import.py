"""import"""
#se utiliza para poder importar una biblioteca (archivo que contiene un conjunto de funciones. se llama de la sig manera:
#import nombreBiblioteca

import random

def aleatorio(inf,sup):
    numAle=random.randiant (inf,sup)       #la llamada a la función tiene la sig forma: nombreBiblioteca.nombreFuncion
    return numAle

def main3():
    print(aleatorio(10,30))
    print(aleatorio(10,30))
    
main3()