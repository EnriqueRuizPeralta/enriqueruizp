from abc import ABC

#import self as self


class ClaseHerencia (ABC):
    _numero1 = int(0)
    _numero2 = int(0)
    _numero3 = int(0)
    __total = bool()

    #METODO CONSTRUCTOR
    def __init__(self,numero1,numero2,numero3):
        self._numero1 = numero1
        self._numero2 = numero2
        self._numero3 = numero3


    @staticmethod
    def Resta(self):
         pass

    @staticmethod
    def Suma(self):
        pass

    @staticmethod
    def Division(self):
        pass


class ClaseResta(ClaseHerencia):
    __total = bool(0)

    def __init__(self,numero1,numero2,numero3):
        ClaseHerencia.__init__(self,numero1,numero2,numero3)
        self.__numero1 = numero1
        self.__numero2 = numero2
        self.__numero3 = numero3
        self.Resta()

    def Resta(self):

        if self.__numero1 - self.__numero2 == self.__numero3 or self.__numero2 - self.__numero1 == self.__numero3:
            self.__total = True

        else:
            self.__total = False
            return self.__total

    def getRestas(self):
        return self.__total


class SumaResultad(ClaseHerencia):
    __total2 = bool(0)

    def __init__(self,numero1,numero2,numero3):
        ClaseHerencia.__init__(self,numero1,numero2,numero3)
        self.__numero1 = numero1
        self.__numero2 = numero2
        self.__numero3 = numero3
        self.Suma()

    def Suma(self):
        if self.__numero1 + self.__numero2 == self.__numero3 or self.__numero2 + self.__numero1 == self.__numero3:
            self.__total2 = True

        else:
            self.__total = False
            return self.__total2

    def getSumas(self):
        return self.__total2


class DivisionResultado(ClaseHerencia):
     __total3 = bool(0)

     def __init__(self, numero1, numero2, numero3):
         ClaseHerencia.__init__(self, numero1, numero2, numero3)
         self.__numero1 = numero1
         self.__numero2 = numero2
         self.__numero3 = numero3
         self.Division()

     def Division(self):
         if self.__numero1 / self.__numero2 == self.__numero3 or self.__numero2 / self.__numero1 == self.__numero3:
             self.__total3 = True

         else:
             self.__total3 = False
             return self.__total3

     def getDivisiones(self):
         return self.__total3














