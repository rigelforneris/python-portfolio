class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class PessoaFisica(Pessoa):
    def __init__(self, CPF, nome, idade):        
        Pessoa.__init__(self, nome, idade)
        self.CPF = CPF

class PessoaJuridica(Pessoa):
    def __init__(self,CNPJ, nome, idade):        
        Pessoa.__init__(self,nome, idade)
        self.CNPJ = CNPJ

p1 = Pessoa('Rigel', 29)

p_fisica = PessoaFisica('11111111111', 'Rigel', '29')

print(p_fisica.CPF)
print(p_fisica.idade)
print(p_fisica.nome)