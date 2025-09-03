class A:
    def method(self):
        print ("Method from A")
class B(A):
    def method(self):
        print ("Method from B")
class C(A):
    def method(self):
        print ("Method from C")
class D(B, C):
    def method(self):
        print ("Method from D")
        
d = D()

print(D.mro())
d.method()