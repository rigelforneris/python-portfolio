class Carro:
    def __init__(self, marca, modelo, cor):
        self.marca = 'marca'
        self.modelo = 'modelo'
        self.cor = 'cor'
    def __str__(self):
        return '<%s, %s ,%s>' % (self.marca, self.modelo, self.cor)
    def __repr__(self):
        return '<Carro> %s' % str(self)

c = Carro('Honda', 'Fit', 'Preto')

print(c)