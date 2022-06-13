class PadreNumero:
    __numero1 = int(0)
    __numero2 = int(0)
    __numero3 = int(0)
    __total = bool(0)

    def __init__(self,numero1,numero2,numero3):
        self.__numero1 = numero1
        self.__numero2 = numero2
        self.__numero3 = numero3
        self.__Resta()

    def Resta(self,numero1,numero2,numero3):
        self.__numero1 = numero1
        self.__numero2 = numero2
        self.__numero3 = numero3

    def get_Resta(self):
        return self.__total

    def get_Suma(self):
        return self.__total

    def get_Division(self):
        return self.__total

    def Resta(self):
        if self.__numero1 - self.__numero2 == self.__numero3 or self.__numero2 - self.__numero1 == self.__numero3:
            self.__total = True

        else:
            self.__total = False
            return self.__total

    def Suma(self):
        if self.__numero1 + self.__numero2 == self.__numero3 or self.__numero2 + self.__numero1 == self.__numero3:
            self.__total = True

        else:
            self.__total = False
            return self.__total


    def Division(self):

        if self.__numero1 / self.__numero2 == self.__numero3 or self.__numero2 / self.__numero1 == self.__numero3:
            self.__total = True

        else:
            self.__total = False
            return self.__total











