import os
print("Diretório atual:")
print(os.getcwd())

print("Arquivos no diretório atual:")
print(os.listdir(os.getcwd()))

print("Listar arquivos no diretório em questão:")
print(os.listdir("códigos/aula_01_arquivos"))

print(os.path.exists("/home/luana/Área de Trabalho/2025.2/DES_PER/códigos/aula_01_arquivos/02_arquivo_txt.py"))
print(os.path.exists("./arquivos/02_alunos.txt"))

with open("códigos/aula_01_arquivos/arquivos/02_alunos.txt","r") as file:
    linha = file.readline() 
    #print(linha)
    while(linha):
        #.strip() remove espaços em branco e quebra de linhas extras
        print(linha.strip())
        linha = file.readline()
