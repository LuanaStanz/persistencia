#Swagger UI, an interactive web-based interface for exploring and testing APIs -> so colocar /docs no link original

#api é uma interface como um cliente num restaurante
#api pega dd p/ vc consumir
#api cria o menu
#uvicorn sobe o menu p/ que o cliente tenha acesso a esses serviçps

# pip install fastapi uvicorn pandas -> #uvicorn é o servidor
#para executar:
#uvicorn main:app --reload
#uvicorn códigos.aula_05_fastapi.main:app --reload

from fastapi import FastAPI, HTTPException #400,500
from pydantic import BaseModel#descrever modelo. mapear todas as entidades, todas minhas entidades vão herdar do Basemodel
#p/ validação de dados 
#BaseModel é uma classe base para criar seus próprios modelos de dados. permitindo Validar automaticamente os tipos de dados recebido...
# Um model pode representar uma entidade (como um aluno, produto, pedido) que existe no banco de dds. Mas no contexto do Pydantic, ele é mais usado para validar e estruturar dados.
import pandas as pd
#import time
#import asyncio  #simular acesso simultaneo

#iniciar o aplicativo (API)
app = FastAPI() #obj

#contador_id e alunos_df são variáveis GLOBAIS!
contador_id = 1 #solução tecnica alternativa
alunos_df = pd.DataFrame(columns = ["id","nome","curso","IRA"]) #coleção da minha base de dds
#não confundir id com index que é do próprio dataFrame

#modelo para a entidade Aluno
class Aluno(BaseModel): 
    nome: str
    curso: str
    IRA: float

#serviço de criação de um Aluno
@app.post("/alunos") #metodo http #criar rota
def criar_aluno(aluno: Aluno):  #recebe obj do tipo Aluno. vindo do request?
    
    #dizendo ao Python que as variáveis que serão modificadas são GLOBAIS
    global alunos_df, contador_id
    
    novo_aluno = {
        "id": contador_id, #meu id pro meu banco de dds
        "nome": aluno.nome,
        "curso": aluno.curso,
        "IRA": aluno.IRA
    }
    
    #forma com o DataFrame._append
    alunos_df = alunos_df._append(novo_aluno, ignore_index = True)
    #forma com o concat
    #alunos_df = pd.concat([alunos_df, pd.DataFrame([novo_aluno])], ignore_index = True)
    contador_id = contador_id + 1 #python acha que tá criando variavel novamente
    #logo, tenho que dizer que é variavel global
    return {
        "mensagem": "Aluno criado com sucesso!",
        "aluno": novo_aluno
    }

#serviço de listagem de TODOS os alunos
@app.get("/alunos") #rota http
def listar_alunos():
    return alunos_df.to_dict(orient = "records") #dict