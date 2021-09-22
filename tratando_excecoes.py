# COM TRATAMENTO DE EXCEÇÕES #

while True:
    try:
        x = int(input('Insira um valor: '))
        print(x)
        break
    except ValueError:
        print(f'Insere aí um número inteiro, deixa de graça.')

# LOOP WHILE TRUE NORMAL #

while True:
    x = int(input('Insira um valor: '))
    if x >= 0 and x <= 10:
        print(x)
        break
    else:
        print(f'Insere aí um número até 10, deixa de graça')
        # Se o valor inserido não for inteiro, o código irá parar
        # já que o erro não foi tratado.
