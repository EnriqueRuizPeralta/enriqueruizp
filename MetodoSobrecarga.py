class SobrecargaMetodos:
  """
     ESTA CLASE SERA PARA CREAR LA SOBRE CARGA DE METODOS
  """
    #ATRIBUTOS
  __numero1 = int(0)
  __numero2 = int(0)
  __numero3 = int(0)
  __resultado = bool()


  def __init__(self,numero1,numero2,numero3,resultado):
      self.__numero1 = numero1
      self.__numero2 = numero2
      self.__numero3 = numero3
      self.__resultado = resultado

  def __str__(self):
      return "El resultado de la resta de " + str(self.__numero1) + " menos" + str(self.__numero2) + str(self.__resultado) + "" + str(self.__numero3)

  def evaluarResta(self, numero1, numero2, numero3):
      self.__numero3 = numero3
      self.__numero2 = numero2
      self.__numero1 = numero1

      if self.__numero1 - self.__numero2 == self.__numero3 or self.__numero2 - self.__numero1 == self.__numero3:
          self.__resultado = True
          return self.__resultado
      else:
          self.__resultado = False
          return self.__resultado
