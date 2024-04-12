valor1 = float(input())
operador = input()
valor2 = float(input())

resultado = 0
while (valor1 != -1) and (valor2 != -1):
        
    if operador == '+':
        resultado = valor1 + valor2
    elif operador ==  '-':
        resultado = valor1 - valor2
    elif operador ==  '*':
        resultado = valor1 * valor2
    elif operador ==  '/':
        resultado = valor1 / valor2    
    else:
        print('operador inválido')

    print(resultado)
    valor1 = float(input())
    operador = input()
    valor2 = float(input())
