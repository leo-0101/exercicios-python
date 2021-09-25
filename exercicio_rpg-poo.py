class Personagem:
    # PRECISA SER UM ATRIBUTO BASE PARA NÃO DAR PROBLEMA #
    vida = 150
    mana = 100
    inteligencia = 30
    forca = 30
    agilidade = 30
    carisma = 20

    def __init__(self, nome):
        self.nome = nome

    def atacar(self, inimigo):
        inimigo.vida -= self.forca
        print(f'O {self.nome} atacou e tirou {self.forca} de pontos do {inimigo.nome}')


class Guerreiro(Personagem):

    inteligencia = 10
    agilidade = 20
    forca = 80

    def __init__(self, nome):
        self.nome = nome
        # Inicialmente eu havia reescrito esse método em todas as outras classes,
        # mas não é necessário. Se tirar, ok. Se deixar, ok também, não muda nada.

    def esmagar(self, inimigo):
        inimigo.vida -= 2*self.forca
        print(f'O guerreiro {self.nome} esmagou o {inimigo.nome} e tirou {2*self.forca} pontos de vida!')


class Mago(Personagem):

    inteligencia = 80
    forca = 10
    agilidade = 20

    def magia(self, inimigo):
        inimigo.vida -= 2*self.inteligencia
        print(f'O mago {self.nome} lançou uma bola de fogo no {inimigo.nome} e tirou {2*self.inteligencia} de vida!')


class Bardo(Personagem):

    carisma = 70
    inteligencia = 20
    forca = 10
    agilidade = 20

    def curar(self, aliado):
        aliado.vida += 2*self.carisma
        print(f'O bardo {self.nome} curou seu aliado {aliado.nome} com {2*self.carisma} pontos de vida!')


class Arqueiro(Personagem):

    agilidade = 80
    forca = 20
    inteligencia = 20
    carisma = 10

    def flechar(self, inimigo):
        inimigo.vida -= 2*self.agilidade
        print(f'O arqueiro {self.nome} flecha o {inimigo.nome} e tira {2*self.agilidade} pontos de vida!')


g1 = Guerreiro('Leo')
m1 = Mago('Leonidas')
b1 = Bardo('Rodrigo')
a1 = Arqueiro('Carlos')

# Atacar é um método da classe pai que todos tem em comum,
# sendo assim, todos podem usar.
a1.atacar(b1)
g1.atacar(b1)
b1.atacar(b1)
m1.atacar(b1)
