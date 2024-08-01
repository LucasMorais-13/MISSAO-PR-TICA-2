saida = ''

def adicao(x,y):
    return x + y

def subtracao(x,y):
    return x - y

def divisao(x,y):
    return x / y

def multiplicacao(x,y):
    return x * y

def calculadora(x,y,sinal):
    if sinal == '+':
        print(adicao(numero1,numero2))
    elif sinal == '-':
        print(subtracao(numero1,numero2))
    elif sinal == '/':
        if numero1 == 0:
            print("Divisão por 0 não é aceita! ")
        elif numero2 == 0:
            print("Divisão por zero não é aceita! ")
        else:
            print(divisao(numero1,numero2))
    elif sinal == '*':
        print(multiplicacao(numero1,numero2))
    else:
        print("Sinal desconhecido")

while saida != "n":
    numero1 = int(input("Infome primeiro valor: "))
    numero2 = int(input("Informe segundo valor: "))
    sinal = input("informe operação: ")
    calculadora(numero1,numero2,sinal)
    saida = input("Deseja continuar ou não executando o programa? DIgite n ou N para sair: ").lower()