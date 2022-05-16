from Herencia import*

def main():
    print("RESTA")
    resultado=ClaseResta(50,25,25)
    print(resultado.getRestas())

    print("SUMA")
    resultado2=SumaResultad(50,50,100)
    print(resultado2.getSumas())

    print("DIVISION")
    resultado3=DivisionResultado(10,2,5)
    print(resultado3.getDivisiones())


if __name__=="__main__":
    main()