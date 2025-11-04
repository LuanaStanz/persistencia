#pip install bs4
import requests
from bs4 import BeautifulSoup # pulling data from HTML and XML

with open("jogadas.html", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

#calcular quandas vezes jogador 1 venceu o pedra papel tesoura
table = soup.find("table")
jogadas = table.find_all("td")
jogadas = [td.get_text().split("\n") for td in jogadas ]
print(jogadas)
contador = 0
index_list = []
for i in range(len(jogadas)-1):
    jogada1 = jogadas[i]
    jogada2 = jogadas[i+1]
    
    print(jogada1, jogada2)
    i += 2

    #if (jogador1 == "Pedra" and jogador2 == "Tesoura") or
#for td in jogadas:
    #jogadas += td.get_text().split("\n")


    #if td.attrs.get("class") and td.attrs.get("class")[0] == "nota":
    #    contador += 1
    #    media += float(td.string)
