from proyecto import *
from MetodoSobrecarga import SobrecargaMetodos
from ClaseResta import RestaAbs



def main():

    #llamada de clase abstracta
    print(RestaAbs.Resta.restadoraDelase(50,25,25))


   #Llamada al Metodo de clase
    print(Resta.restadoraDelase(50, 25, 24))
    print("")

    # Llamada al metodo constructor e instancia
    Rst = Resta(50, 25, 25)
    # Llamada al metodo de instancia
    print(Rst.restadora1(50, 25, 27))


    RESTA1 = SobrecargaMetodos(50,25,25," es igual al numero 3 el cual es  ")
    RESTA2 = SobrecargaMetodos(50,25,65, " No coincide con el numero 3 el cual es ")
    print(RESTA1)
    print(RESTA2)



if __name__ == "__main__":
    main()
