"""
Escriba un algoritmo que dados tres números indique si el tercero es el 
resultado de la resta entre los dos primeros: 1) el primero menos el segundo 
y 2) el segundo menos el primero.
"""


class Resta:
    __numero1 = int(0)
    __numero2 = int(0)
    __numero3 = int(0)
    __resultado = bool()



    #Metodo Construtor
    def __init__(self, numero1, numero2, numero3,):
        self.__numero3 = numero3
        self.__numero2 = numero2
        self.__numero1 = numero1




    def evaluarResta(self,numero1,numero2,numero3):

      if self.__numero1 - self.__numero2 == self.__numero3 or self.__numero2 - self.__numero1:
       self.__resultado = True

      else:
       resultado = False


    #METODO DESTRUCTOR
    def _del__(self):
      self.restadoraDelase()
      self.evaluarResta()

    def get_restadoraDelase(self):
          return self.__resultado

    def get_evaluarResta(self):
        return self.__numero3



    # Metodo de clase
    @classmethod
    def restadoraDelase(cls, numero1, numero2, numero3):

        if numero1 - numero2 == numero3 or numero2 - numero1 == numero3:
            resultado = True

        else:
            resultado = False
            return resultado



    # Metodo de instancia
    def restadora1(self,  numero1, numero2, numero3):
        self.__numero3 = numero3
        self.__numero2 = numero2
        self.__numero1 = numero1

        if self.__numero1 - self.__numero2 == self.__numero3 or self.__numero2 - self.__numero1 == self.__numero3:
            self.__resultado = True
            return self.__resultado
        else:
            self.__resultado = False
            return self.__resultado









