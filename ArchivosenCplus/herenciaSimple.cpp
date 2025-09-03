#include <iostream>


class Animal {
    public:
    virtual ~Animal() = default;
    void respirar() const { std::count << "Respirando..." << std::endl;}
}

struct Perro : public Animal {
    void ladrar() const { std::cout << "Guau Guau!" << std::endl;}
}

struct Gato : public Animal {
    void maullar() const { std::cout << "Miau Miau!" << std::endl;}
}

int main() {
    Perro miPerro;
    Gato miGato;

    miPerro.respirar();
    miPerro.ladrar();

    miGato.respirar();
    miGato.maullar();

    return 0;
}