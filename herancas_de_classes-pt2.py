class Soldado:
    def __init__(self, nome, idade):
        self.nome = nome
        self.nome = idade

    def atirar(self):
        print('O soldado está atirando ...')


class Aliado(Soldado):
    def __init__(self, nome, idade, patente):
        self.nome = nome
        self.idade = idade
        self.patente = patente

        # Pegamos a classe e a reescrevemos para que possa ser adicionado
        # o atributo 'patente', que só é dada, nesse exemplo, ao soldado Aliado.


class Inimigo(Soldado):
    pass


aliado1 = Aliado('Leonardo', '23', 'Sargento')
inimigo1 = Inimigo('Natan', '20')

# Sargento é uma característica específica do Aliado,
# logo o Inimigo não terá acesso a ela e o programa apontará um erro.


print(f'A patente do soldado aliado é: {aliado1.patente}')
print(f'A patente do soldado inimigo é: {inimigo1.patente}')
