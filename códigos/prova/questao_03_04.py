import httpx
#PS: servidor no main.py
#api registra e consulta notas de alunos mantendo dados em df

BASE_URL = "http://127.0.0.1:8000"

def adicionar_aluno(nome, nota):
    resp = httpx.post(
        f"{BASE_URL}/alunos",
        json = {"nome":nome,"nota":nota}
    )
    print("Adicionando...\n", resp.json())
    return resp

def obter_nota(nome):
    resp = httpx.get(f"{BASE_URL}/alunos/{nome}")
    print("Obtendo...\n", resp.json())
    return resp.json()

def listar_alunos():
    resp = httpx.get(f"{BASE_URL}/alunos")
    print("Listando...\n", resp.json())
    return resp.json()

adicionar_aluno("Matias", 5.2)
obter_nota("Jefferson")
obter_nota("Matias")
obter_nota("Clara")
listar_alunos()
