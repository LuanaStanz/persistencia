gravar = []

with open("prova/dados_alunos.txt","r") as file:
    linha = file.readline() 
    #print(linha)
    while(linha):
        #print(linha.split('#'))
        linha = file.readline()
        gravar.append(linha.split('#'))

soma = 0
for x in range(0, len(gravar)-1):
    #print(gravar[x][2])
    #print(type(gravar[x][2])) #str
    gravar[x][2] = float(gravar[x][2])
    #print(type(gravar[x][2])) #float
    soma += gravar[x][2]

media = soma / (len(gravar))
big = max([float(gravar[x][2]) for x in range(0, len(gravar)-1)])
small = min([float(gravar[x][2]) for x in range(0, len(gravar)-1)])

print(f"Média da turma: {media}")

for x in range(0, len(gravar)-1):
    if float(gravar[x][2]) == big:
        b_name = gravar[x][0]
    if float(gravar[x][2]) == small:
        s_name = gravar[x][0]
print(f"Maior nota: {big} ({b_name})")
print(f"Menor nota: {small} ({s_name}")
