import sys

texto = "   exemplo com espaços   \n"
print("ANTES:"+repr(texto)+"<--") #repr() mostra os caracteres invisíveis como \n e espaços.
print("DEPOIS:"+repr(texto.strip())+"<--")
print("-->"+texto.lstrip()+"<--")  # remove da esquerda (início)
print("-->"+texto.rstrip()+"<--") #rstrip() → remove da direita (fim)

#remover todos espaços
mensagem = "rg     rgv ag a   aw ra gr r g  wgw g wg   waeg   we"
sem_espacos = mensagem.replace(" ", "")
print(sem_espacos)
#remover todos espaços em branco, tb, quebra de linha
import re
mensagem = "rg     rgv ag a   aw ra gr r g  wgw g wg   waeg   we\n"
sem_espacos = re.sub(r"\s+", "", mensagem) #caso queira só consecutivos substitua por " " em vez de ""
print(sem_espacos)

#ler teclado
linha =  sys.stdin.readline()
while linha:
    print("-->" + linha.strip() + "<--") #tira espaços e quebras de linhas no inicio e no final
    linha = sys.stdin.readline()


