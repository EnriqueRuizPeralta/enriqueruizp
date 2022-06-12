import java.io.*;
import java.util.ArrayList;

public class pruebaArchivos {

    private ArrayList<String> contenidoArchivo = new ArrayList<>();
    private ArrayList<Restacodigo> listaEntradas = new ArrayList<>();
    private final String rutaWindows = "C:\\Users\\GIGABYTE\\IdeaProjects\\CodigoJavaEnrique\\src\\datos.txt";
    private final String rutaLinux = "/C:/Users/GIGABYTE/IdeaProjects/CodigoJavaEnrique/src/datos.txt";

    public ArrayList<String> getContenidoArchivo() {
        return contenidoArchivo;
    }

    public ArrayList<Restacodigo> getListaEntrada() {
        return listaEntradas;
    }

    public void leerArchivo(){
        LeerArchivo leer = new LeerArchivo();
        this.contenidoArchivo =
                leer.leerArchivo(this.rutaLinux);
        for (int i=0; i < this.contenidoArchivo.size();i++){
            String linea = this.contenidoArchivo.get(i);
            String elementosLinea[] = linea.split("#");
            try {
                int Numero1= Integer.parseInt(elementosLinea[0]);
                int Numero2 = Integer.parseInt(elementosLinea[1]);
                int Numero3 = Integer.parseInt(elementosLinea[2]);
                listaEntradas.add(new Restacodigo(Numero1,Numero2, Numero3));
            } catch (NumberFormatException ex){
                ex.printStackTrace();
                listaEntradas.add(new Restacodigo(0,0,0));
            }
        }
    }

    public void escribirArchivo(ArrayList<Restacodigo> lista){
        String archivo = "resultados.csv";
        File f = new File(archivo);
        //Escritura
        try{
            FileWriter w = new FileWriter(f);
            BufferedWriter bw = new BufferedWriter(w);
            PrintWriter wr = new PrintWriter(bw);
            wr.write("");
            wr.append("NUMERO1,NUMERO2,NUMERO3, RESULTADO\n");
            for (int i=0; i < lista.size(); i++){
                wr.append(lista.get(i).getNumero1() +
                        "," + lista.get(i).getNumero2() +
                        "," + lista.get(i).getNumero3() + "," +
                        lista.get(i).getResultado() + "\n");
            }
            wr.close();
            bw.close();
        }catch(IOException e){

        }
    }

    public static void main (String args[]){
        pruebaArchivos prueba = new pruebaArchivos();
        prueba.leerArchivo();
        for (int i=0; i < prueba.getListaEntrada().size(); i++){
            System.out.println(prueba.getListaEntrada().get(i).getNumero1() +
                    "\t" + prueba.getListaEntrada().get(i).getNumero2() +
            "\t" + prueba.getListaEntrada().get(i).getNumero3() + "\t" +
                    prueba.getListaEntrada().get(i).getResultado());
        }
        prueba.escribirArchivo(prueba.getListaEntrada());

    }
}
