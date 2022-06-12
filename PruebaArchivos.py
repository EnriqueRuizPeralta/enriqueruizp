from abc import ABCMeta

class RestaAbs(ABCMeta):

    # Método de clase
    @staticmethod
    def Resta(numero1,numero2,numero3):
        if numero1 -numero2 == numero3 or numero2 - numero1 == numero3:
            total = True

        else:
            total = False
        return total

class pruebaArchivos:

    def leerArchivo(self, archivo):
        file = open(archivo, 'r')
        lineas = []
        lineas_archivo = []
        for linea in file.readlines():
            lineas.append(linea.replace('\n', '').split(";"))
        file.close()
        for f in range(0, len(lineas)):
            try:
                lineas_archivo.append([int(lineas[f][0]), int(lineas[f][1]), float(lineas[f][2])])
            except ValueError:
                lineas_archivo.append([0,0,0.0])
        return lineas_archivo

    def calcularResta(self, lista):
        resultados = []
        for f in range(0, len(lista)):
            resultados.append(RestaAbs.Resta(
                lista[f][0],lista[f][1],lista[f][2]))
        return resultados

    def guardarResultados(self, entrada, resultados):
        file = open("resultados.txt", 'w')
        file.write('numero1,numero2,numero3,resultados\n')
        for f in range(0, len(entrada)):
            linea = str(entrada[f][0]) + '#' + \
                    str(entrada[f][1]) + '#' + str(entrada[f][2]) + \
                    '#' + str(resultados[f]) +'\n'
            file.write(linea)
        file.close()

if __name__ == "__main__":
    prueba = pruebaArchivos()
    archivo = []
    archivo = prueba.leerArchivo("datos.txt")
    print(archivo)
    resultado = prueba.calcularResta(archivo)
    print(resultado)
    prueba.guardarResultados(archivo, resultado)