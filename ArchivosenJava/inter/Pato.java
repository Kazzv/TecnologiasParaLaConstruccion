package inter;

public class Pato extends Animal implements Volador {
    private String colot;

    public Pato(int age, String color) {
        super(age);
        this.color = color;
    }

    @Override
    public void hacerRuido() {
        System.out.println(".()");
    }

    
}
