notas = []
para = 0
while para != -1:
    notas.append(float(input("Informer a nota: ")))
    para = notas[-1]
    

notas.remove(-1)

soma = sum(notas)

media = soma/len(notas)

if media >= 7:
    print('Aluno APROVADO!')
else:
    print('Alunos REPROVADO!!')
