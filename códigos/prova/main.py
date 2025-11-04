from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
#uvicorn main:app --reload

class Aluno(BaseModel):
    nome: str
    nota: float

app = FastAPI()

#contador_id e alunos_df são variáveis GLOBAIS!
contador_id = 4
alunos_df = pd.DataFrame(
    {
        "id": [1,2,3],
        "nome": ["Jefferson", "Wladimir", "Fábio"],
        "nota": [6.7, 8.3, 3.2]
    }
)

#post /alunos
#recebe nome, nota
    #se já existir atualizar nota
    #se não criar aluno
@app.post("/alunos")
def adicionar_aluno(aluno: Aluno):
    global alunos_df, contador_id
    #se já existir atualizar nota
    if not alunos_df[alunos_df["nome"]== aluno.nome].empty:
        aluno_idx = alunos_df.index[alunos_df["nome"] == aluno.nome]
        alunos_df.loc[aluno_idx, "nota"] = aluno.nota
        return {
            "mensagem": f"Aluno {aluno.nome} atualizado com sucesso! Nota {aluno.nota}",
            "aluno": alunos_df.loc[aluno_idx].to_dict(orient="records")[0]
        }
    
    #se não criar aluno
    else:
        novo_aluno = {
            "id": contador_id,
            "nome": aluno.nome,
            "nota": aluno.nota
        }
        
        alunos_df = alunos_df._append(novo_aluno, ignore_index = True)
        contador_id = contador_id + 1
        return {
            "mensagem": "Aluno criado com sucesso!",
            "aluno": novo_aluno
    }
#get /alunos/{nome} -> retorna sua nota caso aluno exista
#se não mensagem  dizendo que aluno não foi registrado
@app.get("/alunos/{nome}")
def obter_nota(nome: str):
    filtro = alunos_df["nome"] == nome
    aluno = alunos_df[filtro]
    if aluno.empty:
        raise HTTPException(status_code=404, detail=f"Aluno {nome}, não encontrado")
    return aluno.to_dict(orient="records")[0]

#listagem de TODOS os alunos
@app.get("/alunos")
def listar_alunos():
    return alunos_df.to_dict(orient = "records")
