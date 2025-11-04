#r: read 
with open("códigos/aula_01_arquivos/arquivos/06_saida.txt","r",encoding="utf-8") as file:
    file.read()
#a: append
with open("códigos/aula_01_arquivos/arquivos/06_saida.txt","a",encoding="utf-8") as file:
    file.write("d+\n")
#w: write - apaga tudo de antes, substitui conteúdo anterior
with open("códigos/aula_01_arquivos/arquivos/06_saida.txt","w") as file:
    file.write("d+\n")
#x: exclusive criation - cria erro se já existir
#r+: read & write - abre.
#w+: write & read - abre. Apaga o conteúdo anterior.
#a+: append & read - abre. adição no final. Cria se não existir.
#x+: create&read/write - Cria novo arquivo para leitura e escrita. Erro se já existir.

#tb existem os modificadores binários

#Outros usos do 'with'
import zipfile
with zipfile.ZipFile("arquivo.zip", "r") as zip:
    zip.extractall()

with conexao.cursor() as cursor:
    cursor.execute("SELECT * FROM tabela")

from threading import Lock
lock = Lock()
with lock:
    # código protegido por trava

#próprio obj
import time

class Temporizador:
    def __enter__(self):
        self.inicio = time.time()
        print("Iniciando temporizador...")
        return self  # opcional, mas útil se quiser usar dentro do bloco

    def __exit__(self, tipo, valor, traceback):
        fim = time.time()
        print(f"Tempo decorrido: {fim - self.inicio:.2f} segundos")

with Temporizador():
    for i in range(1000000):
        pass  #placeholder quando a sintaxe exige uma instrução, mas você ainda não quer escrever nada ali.
#Quando o with começa, __enter__() é chamado → inicia o cronômetro
#Quando o bloco termina, __exit__() é chamado → calcula o tempo e imprime