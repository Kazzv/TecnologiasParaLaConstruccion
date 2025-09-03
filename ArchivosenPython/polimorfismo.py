class animal:
    def hacer_sonido(self):
        raise NotImplementedError("Función no implementada")
    
class perro(animal):
    def hacer_sonido(self):
        return "Guau"
    
class gato(animal):
    def hacer_sonido(self):
        return "Miau"
    
class caja(self):
    def __init__(self):
        self._items = []
    def meter(self, x):
        self.items.append(x)
    def primero(self):
        return self._items[0]
    
def describir(a):
    if insinstance(a, perro):
        return "Es un perro"    
    elif isinstance(a, gato):
        return "Es un gato"
    else:
        return "Es un animal"
    
def saludar(animal):
    print (animal.hablar())

class MedidorEnergia:
    def energia(self, a:animal):
        if isinstance(a, perro):
            return len(a.hacer_sonido()) * 1.00
    
saludar(perro())
saludar(gato())

c1 = caja()
c2 = caja()
c1.meter(perro())
c2.meter(gato())
print (c1.primero().hacer_sonido())
print (c2.primero().hacer_sonido())

print (describir(perro()))
print (describir(gato()))

m = MedidorEnergia()
e = m.energia(perro())
x = 2

print (e + x)