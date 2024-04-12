def soma(a,b):
    return a+b

def subtrai(a,b):
    return a-b

def multiplacao(a,b):
    return a*b

def divisao(a,b):
    return a/b

valor1 = float(input())
operador = input()
valor2 = float(input())

resultado = 0
while (valor1 != -1) and (valor2 != -1):
        
    if operador == '+':
       resultado = soma(valor1,valor2)
    elif operador ==  '-':
        resultado = subtrai(valor1,valor2)
    elif operador ==  '*':
        resultado = multiplacao(valor1,valor2)
    elif operador ==  '/':
        resultado = divisao(valor1,valor2)    
    else:
        print('operador inválido')

    print(resultado)
    valor1 = float(input())
    operador = input()
    valor2 = float(input())
