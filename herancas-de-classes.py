class Funcionario:

    salario = 1500

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def trabalhar(self):
        print(f'O funcionário {self.nome} está trabalhando ...')

    def descansar(self):
        print(f'O funcionário {self.nome} está descansando ... ZzZzZzZ')

    # PS: AS SUB-CLASSES PODEM TER TAMBÉM MÉTODOS ESPECÍFICOS DELA
    # SEM QUE PRECISE EXISTIR NA SUPER CLASSE, COMO MOSTRADO EM ALGUNS EXEMPLOS ABAIXO.


class Dono(Funcionario):
    salario = 3000

    def trabalhar(self):
        print(f'O dono da loja está conversando com investidores ...')

    def descansar(self):
        print('O dono da loja está descansando ... ZzZzZzZ')


class Gerente(Funcionario):
    # O método acima entre parênteses equivale a uma herança.
    # A classe 'Gerente' está herdando os atributos da classe 'Funcionário'.

    salario = 2000
    # Está fazendo um override, isto é, sobreescrevendo o salário para sua nova sub-classe/herança.

    def trabalhar(self):
        print(f'O gerente {self.nome} está gerenciando a loja ...')
        # Aqui também sobreescrevemos o método para esta sub-classe.
        # Podemos fazer assim para todas os outros métodos da super classe caso queiramos.

    def conferir_estoque(self):
        print(f'O gerente {self.nome} está conferindo o estoque ...')


funcionario1 = Funcionario('Leonardo', 23)
gerente1 = Gerente('Caio', 30)
dono1 = Dono('Julio', 45)

print(funcionario1.salario)
print(gerente1.salario)
# Aqui mostramos que, de fato, o salário foi alterado para sua sub-classe.

funcionario1.trabalhar()

gerente1.trabalhar()

funcionario1.descansar()

gerente1.descansar()

gerente1.conferir_estoque()

dono1.trabalhar()

dono1.descansar()

# Aqui, por fim, é confirmado por meio de vários exemplos que
# as heranças foram herdadas da classe 'Funcionario'.
