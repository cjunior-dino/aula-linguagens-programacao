nome = str(input("Informe o nome: "))

remova = int(input('Informe uma posição de 0 a ' + str(len(nome)-1) + ' para alterar ou remover a letra: '))

if nome[remova] == 'r':
    nome = nome.replace(nome[remova],"s")
elif nome[remova] == 'm':
    nome = nome.replace(nome[remova],"n")
else:
    nome = nome.replace(nome[remova],"")

print(nome)
