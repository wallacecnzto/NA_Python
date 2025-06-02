n = int(input("Quantos alunos serao digitados? "))
nomes = [0 for x in range(n)]
notas_primeiro_semestre = [0 for x in range(n)]
notas_segundo_semestre = [0 for x in range(n)]
media = 0

for i in range(n):
    print(f"Digite nome, primeira e segunda nota do {i + 1}º aluno:")
    nomes[i] = input()
    notas_primeiro_semestre[i] = float(input())
    notas_segundo_semestre[i] = float(input())
    
for i in range(n):
    media = (notas_primeiro_semestre[i] + notas_segundo_semestre[i]) / 2
    if media >= 6.0:
        print(nomes[i])

