package Herencia;

public class mainHerencia {
    public static  void main(String[]args){
        System.out.println("SUMA");
        ClaseSuma resultado = new ClaseSuma(45,34,34);
        System.out.println(resultado.getSonIguales());

        System.out.println("DIVISION");
        ClaseDivision resultado2 = new ClaseDivision(45,35,35);
        System.out.println(resultado2.getSonIguales());

        System.out.println("RESTA");
        ClaseResta resultado3 = new ClaseResta(50,25,25);
        System.out.println((resultado3.sonIguales));

    }
}
