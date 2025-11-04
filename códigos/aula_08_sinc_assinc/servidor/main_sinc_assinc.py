#uvicorn main_sinc_assinc:app --reload
from fastapi import FastAPI
import time
import asyncio

app = FastAPI()

#default: sincrona - chamadas sequenciais
@app.get("/sinc") #bloqueia servidor
# trabalhar com dados em memória/arquivo, cálculos grandes, ou bases de dados blocantes, use 
# rotas sincronas
def rota_sincrona():
    time.sleep(2)  # bloqueia a execução por 2 segundos
    return {"tipo": "SÍNCRONA"}

# trabalhar com chamadas assíncronas dentro da API, como por exempo, httpx, requests
# acessar uma base de dados com asyncpg ou simulando com o asyncio
@app.get("/assinc") #permite paralelismo
async def rota_assincrona():
    # simulando uma chamada assincrona!
    await asyncio.sleep(2) # não bloqueia o loop de eventos
    return {"tipo": "ASSÍNCRONA"}