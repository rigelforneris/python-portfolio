virtualenv


paradigma: forma de organizar o código

Modelo imperativo - linguagem C
Python é multi paradigma

POO é mais próxima de como nos expressamos no mundo real


Alan kay: Pai Da programação orientada a objetos

* reutilização de código é melhor
* Criação de bibliotecas é mais simples

criador de python: ?

*Maior agilidade

Paradigmas:

Procedural: Chamadas de procedimentos - Linguagens como C, python, pascal entre outras suportam este paradigma
POO: Objetos que possuem propriedades, que são os atributos e operações que são métodos ou funções
Funcional: ?

carro

objeto som


Marcador para inteiros: %d

#listas e conjuntos
lista = [10. 'rigel',3.14]

len(lista)

lista[1] #resultado: rigel

c = set()
c.add('10')
c #10

c.add('20')
c #10,20

Dicionários:

d = {'rigel':29}
d['rigel']#29

d = {'rigel':'forneris'}
d['rigel']#forneris

'rigel' in d #true
'camila in d' #false

#tuplas
t = ()
t = (1,2,3,4)
t 

#Entrada de dados

#python2
idade = raw_input('digite sua idade')
#python3
idade = input('Digite sua idade')

#Input SEMPRE retorna valores tipo string a menos que você converta:

idade = int(input('Digite sua idade))

var_pi = float(input('Digite o número PI:'))

#Entrada de dados é um ponto frágil! Nunca se sabe o que o usuário vai digitar


#for

#de 1 até 10
for i in range(1,11):

#Operador ternario

idade = 20

print('maior de idade') if idade >= 18 else print('menor de idade')



trabalhando com arquivos:
Somente leitura:
arq = open('arquivo.txt','r' )
Modo escrita (sobrescrevendo gravações anteriores):
arq = open('arquivo.txt','w' )
Modo escrita (mantendo gravações anteriores):
arq = open('arquivo.txt','a' )
Modo binário:
arq = open('arquivo.txt','b' )
Combinando leitura e escrita:
arq = open('arquivo.txt','r+w' )


Objeto inclui dados e comportamentos
aonde:
dados são campos
comportamentos são os métodos
geralmente os campos são manipulados pelos métodos do objeto, 
o que chamamos de encapsulamento

interagimos com um objeto através dos métodos

não alteramos diretamente os campos, usamos MÉTODOS para trabalhando

os objetos possuem atributos, que podem ser métodos ou atributos 
de dados são os campos.

métodos são o que altera os campos, é como interagimos com o objeto

métodos também são atributos!


lista = []
lista.append(10)

type(lista)


métodos com 2 underscore:

Dunder = métodos ESPECIAIS (definem interfaces)

__add__

__len__ -> lista.__len__()

a notação correta deverá ser: len(lista)

geralmente o dunder é chamado pelo próprio python

sabendo atributos de um determinado objeto:
dir(objeto)

exemplo:

lista = [1,2,3]
lista = list()

dir(lista)

em python tudo é objetos! Não existem tipos primitivos

python tem tipagem forte
praticamente não existe a conversão automática de tipagem

l1 = [1,2,3]
l2 = l1
l2 is l1 -> true - são o mesmo objeto

l3 = l1[:]

l3 is l1 -> false - não são o mesmo objeto

um objeto contém dados e comportamentos




Classes e objetos

classe: definição de um novo tipo de dados, que associa dados 
e operações em uma só estrutura, é visto como um molde, ou modelo.

type('python') -> str

Objeto: Pode ser entendido como uma variável cujo tipo é uma classe
um objeto é uma instancia e uma classe

Um método construtor é sempre chamado quando uma classe é instanciada
é ele que inicializa um novo objeto com os valores padrão



quando usamos "E um(a)" para definir uma classe, utilizamos herança

Herança e composição

Programação Funcional

lambda = palavra chave do python para definir pequenas funções anonimas
elas permitem apenas uma expressão

dobro = lambda x: x * 2
dobro(3) = 6

soma = lambda x, y: x + y
soma(10,20) = 30

Filter - recebe com parametros uma função e uma sequencia, 
por exemplo uma lista, ela executa esta função para cada 
elemento da squencia retornando os elementos para qual a 
função retorna verdadeiro

exemplo:

lista = [1,2,3,4,5,6,7,8,9,10]
filter(lambda x: x % 2 == 0, lista) >> lista em qual posição da
memória o objeto está

list(filter(lambda x: x % 2 == 0, lista)) >> correto

list(map(lambda x: x*2 , lista))



Python usa tipagem dinamica!

Criação de classes

Ao criar uma classe, por convenção, ela deverá ter a 
primeira letra maiúscula!

Deverá ser seguido o guia de estilo PEP8

Instanciando:
obj = MinhaClasse()

ao dar print ele apresenta a classe e o endereço de memória

atributos de instancia e atributos de classe

Atributo é um dado para qual cada objeto tem o seu próprio valores

as mensagens enviadas ao objeto através de métodos podem mudar o valor
de um ou mais atributo, alterando assim o estado do objeto

Podemos setar atributos arbitrariamente em um objeto Instanciando

exemplo:

p = P()
p.x = 5
p.y = 10
p.nome = 'Python'

print(p.x)
print(p.nome)

Programação orientada a objetos é interação entre objetos

Diferença de um metodo para função: todos os métodos tem um 
argumento obrigatório que é convencionalmente chamado de self

self é um argumento para o método, é simplemente uma referencia
para o objeto que o método está sendo invocado

é como se fosse o this

Podemos acessar atributos e métodos do objeto

ao invocar o método não é necessário informar o self

método nada mais é do que uma função que está dentro de uma classe.



Método construtor (ou inicializador)

É uma função definida no python, que define o inicio da classe(?)

self: primeiro parâmetro definido dentro da classe, poderia ser qualquer nome mas usamos self por convenção

o primeiro parâmetro se refere a instancia atual que se encontra o método

Em orientação a objetos uma classe terá em geral atributos, que são as características do modelo 
e os métodos que são as ações que ele poderá fazer, e o construtor ou inicializador, que terá 
a função de inicializar a instância

classe object: a classe "mãe" de todas as classes

class Ponto:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def resetar(self):
        self.x, self.y = 0, 0
    def algo():
        pass

p = Ponto(10,20)
print(p.x, p.y)

Invocando a função resetar à partir do método
p.resetar()

Invocando a função resetar à partir da classe
Ponto.resetar(p)
print(p.x, p.y)

Quando esquecemos do argumento "self" ao criar o método, o python retorna o seguinte traceback:

metodo() takes 0 positional arguments but 1 was given

Porque para inicializar qualquer método na definição da classe é necessário pelo menos 1 argumento, e ele por convenção é o self, pois ele sempre será refernte ao próprio método (como o localhost no linux)

Pacote: coleção de módulos (podem conter outros pacotes)

Um módulo é estruturado em arquivo!

Um pacote é estruturado em diretório
__init__.py é o arquivo que identifica o diretório como pacote (pode ser um arquivo vazio, mas pode conter um código para inicialização do pacote)

um pacote é uma coleção de módulos em um diretório

Fila de prioridades: Ordena os itens de acordo com a dada prioridade

heapq:
métodos heappush e heappop inserem e removem itens de uma lista, que é a fila

A fila é formada por TUPLAS, como por exemplo:

(-prioridade, self.indice, item)

o valor de prioridade é negado para enfileirar os itens da mais alta para a mais baixa prioridade que é o oposto da ordem natural da heappop

a variável indice tem a função de ordenar adequadamente os itens com o mesmo valor de prioridade 

quando se tem um indice que aumenta constantemente os itens são ordenados de acordo com a ordem que foram inseridos

o indice tem uma outra função que é a comparação entre itens com o mesmo nível de prioridade

docstring: definido na pep 257, são strings que inserimos dentro do nosso código com o intuito de fornecer uma explicação sobre o funcionamento do código
Essa string deve ser colocada como a priomeira linha da definição de uma classe, método ou função.
Ela é apresentada no comando help (que doido!!!)

A docstring faz parte do objeto sobre o qual foi definido.

exemplo:

def multiplica(x, y):
    '''Este método retorna a multiplicação de dois números'''
    return x * y

help(multiplica)

ou

multiplica.__doc__

Método mágico: Facilitam alguma lógica interna do python

Toda a classe que criamos, utiliza herança!

Todas as classes do pythons são subclasses da classe mãe object, se não for definido nada, uma classe herdará de object


objetos em python á partir do python 3 herdam da object, se não for passado nenhum argumento ao criar a classe

A subclasse deriva da classe pai, a subclasse extende a classe pai

classe pai = superclasse

super: Palavra reservada para chamarmos o método e os atributos da classe acima

super().__init__(nome, slario,cpf) >> aqui eu chamo o construtor de uma classe

