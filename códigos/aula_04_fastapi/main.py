# pip install fastapi uvicorn pandas -> #uvicorn é o servidor, publica api

#api é uma interface como um cliente num restaurante
#api pega dd p/ vc consumir
#api cria o menu
#uvicorn sobe o menu p/ que o cliente tenha acesso a esses serviçps

from fastapi import FastAPI, HTTPException #400,500
from pydantic import BaseModel #descrever modelo. mapear todas as entidades, todas minhas entidades vão herdar do Basemodel
#p/ validação de dados 
#BaseModel é uma classe base para criar seus próprios modelos de dados. permitindo Validar automaticamente os tipos de dados recebido...
# Um model pode representar uma entidade (como um aluno, produto, pedido) que existe no banco de dds. Mas no contexto do Pydantic, ele é mais usado para validar e estruturar dados.
import pandas as pd
#import time
#import asyncio #simular acesso simultaneo

contador_id = 1 #solução tecnica alternativa
alunos_df = pd.DataFrame(columns =["id", "", ]) #vazio. coleção da minha base de dds
#posso definir logo as colunas deles
#não confundir id com index que é do próprio dataFrame
class Aluno(BaseModel):
    nome: str
    curso: str
    IRA: float

def criar_aluno(aluno: Aluno): #recebe obj do tipo Aluno. vindo do request?
    novo = { #obj novo
        "id": contador_id, #meu id pro meu banco de dds
        "nome": aluno.nome,
        "curso": aluno.curso,
        "IRA": aluno.IRA
    }
#schema seria das regras p/ esse modelo p/ ficar parecido com um banco de dds
#tipos, tamanho dos caracteres, relacionamentos -> biblioteca monguse