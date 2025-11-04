import sys #acesso direto ao interpretador e ao ambiente de execução, permitindo controlar e inspecionar o comportamento do programa.
print("Hello World of Python!!")
print(sys.version) #versão do Python 

#sys.argv #Lista de argumentos passados na linha de comando
#sys.exit([code])#Encerra o programa com um código de status (0 = sucesso)
#sys.path #Lista de diretórios onde o Python procura por módulos
#sys.stdin, stdout, stderr #Manipula entrada, saída e erros padrão
#sys.platform #Identifica o sistema operacional (ex: 'win32', 'linux', 'darwin')
#sys.getsizeof(obj) #Retorna o tamanho (em bytes) de um objeto
#sys.modules #Dicionário com todos os módulos carregados
