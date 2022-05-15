#METODO CONSTRUCTOR

class Resta:

    def __init__(self,resultado):
        self.resultado = resultado

    def __del__(self):
       self.resultado = "El numero 3 no coincide con las restas"
       print("Se ah destruido todo")


Num3 = Resta("Numero3")
Num3.__del__()
print(Num3.resultado)



