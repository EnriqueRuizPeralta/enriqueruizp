package Herencia;
public abstract class PadreNumero {
    protected boolean sonIguales;

    public abstract void evaluarOperadores();

    public boolean getSonIguales(){
        return this.sonIguales;
    }
}
