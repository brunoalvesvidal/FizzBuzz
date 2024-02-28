def fatorial (numero):
    if numero == 0 or numero == 1 :
        return 1
    else :
        return numero * fatorial(numero-1)
    
def resultado():
    while True:
        x = (input('Digite um número inteiro positivo para calcular seu fatorial: '))
        try:
            numero = int(x)
            valor = fatorial(numero)
        finally:
            print(valor)

resultado()
