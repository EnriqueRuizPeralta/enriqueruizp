public class Restacodigo {

    private int numero1;    // EL PRIMER NUMERO DE LA RESTA
    private int numero2;      // EL SEGUNDO NUMERO DE LA RESTA
    private int numero3;          // EL TERCER NUMERO DE LA RESTA
    private  boolean resultado;

    public Restacodigo(int numero1, int numero2, int numero3) {
        this.numero1 = numero1;
        this.numero2 = numero2;
        this.numero3 = numero3;
        this.Restador();
    }

    public int getNumero1() {
        return numero1;
    }
    public void setNumero1(int numero1) {
        this.numero1 = numero1;
    }

    public int getNumero2() {
        return numero2;
    }
    public void setNumero2(int numero2){
        this.numero2 = numero2;
    }

    public int getNumero3() {
        return numero3;
    }
    public void setNumero3(int numero3){
        this.numero3 = numero3;
    }

    public boolean getResultado(){
        return resultado;
    }
    public void setResultado(boolean resultado) {
        this.resultado = resultado;
    }

    //METODO
    public void Restador() {
        if (this.numero1 - this.numero2 == this.numero3 || this.numero2 - this.numero1 == this.numero3) {
            this.resultado = true;

        }  else {
            this.resultado = false;
        }
    }

}