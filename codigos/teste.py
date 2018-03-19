#from poligono import Quadrado  <<< também dá para importar assim
#import poligono
#from poligono import Retangulo

#import modulo.poligono
from modulo.poligono import Quadrado, Retangulo

q = Quadrado(5)
print(q.perimetro())
print(q.area())

r = Retangulo(5, 10)
print(r.area())