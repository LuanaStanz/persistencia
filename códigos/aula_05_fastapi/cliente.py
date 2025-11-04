#pip install httpx
import httpx #equivalente do fetch/axious do JS

BASE_URL = "http://127.0.0.1:8000"
#poderia usar id de aluno que quero pegar

def criar_aluno(): #seria chamado por uma interface gráfica
    resp = httpx.post(
        f"{BASE_URL}/alunos",
        json = {"nome":"Beltrano","curso":"CC","IRA":7.6} #obrigatorio colocar tipo json
    )
    print(resp.json()["mensagem"])
    print(resp.json()["aluno"]["nome"])

def listar_alunos():
    resp = httpx.get(f"{BASE_URL}/alunos")
    print(resp.json())
    
#execuçao
criar_aluno()
criar_aluno()
criar_aluno()
listar_alunos()
