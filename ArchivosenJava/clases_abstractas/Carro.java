package clases_abstractas;

public abstract class Camion {
    protected String marca;
    protected int llantas;
    protected String color;

    public Carro (String marca, int llantas, String color) {
        this.marca = marca;
        this.llantas = llantas;
        this.color = color;
    }

    public void encender() {
        System.err.println("Carro encendido.");
    }

    public abstract void acelerar();
}

