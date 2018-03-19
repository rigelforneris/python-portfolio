class Funcionario:

    def __init__(self, nome, salario, cpf, x):
        self.nome = nome
        self.salario = salario
        self.cpf = cpf
        self.__x = x # <<< não pode ser herdado

    
class Gerente(Funcionario):
    pass

g = Gerente('Leo_babaca','2400','09633214685', 1)
print(g.nome)
